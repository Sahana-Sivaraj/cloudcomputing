# application/frontend/views.py
import requests
from frontend.app import forms
from frontend.app import frontend_blueprint
from frontend import login_manager
from frontend.app.api.UserClient import UserClient
from frontend.app.api.SatlliteClient import SatelliteClient
from flask import render_template, session, redirect, url_for, flash, request

from flask_login import current_user


@login_manager.user_loader
def load_user(user_id):
    return None


@frontend_blueprint.route('/', methods=['GET'])
def home():
    resultsp=[]
    try:
        products = SatelliteClient.get_products()
        if products:
            resultsp=products
        else:
            resultsp={'results': []}
    except requests.exceptions.ConnectionError:
       resultsp= {'results': []}

    return render_template('home/index.html', products=resultsp)


@frontend_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data

            # Search for existing user
            user = UserClient.does_exist(username)
            if user:
                # Existing user found
                flash('Please try another username', 'error')
                return render_template('register/index.html', form=form)
            else:
                # Attempt to create new user
                user = UserClient.post_user_create(form)
                if user:
                    flash('Thanks for registering, please login', 'success')
                    return redirect(url_for('frontend.login'))

        else:
            flash('Errors found', 'error')

    return render_template('register/index.html', form=form)


@frontend_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('frontend.home'))
    form = forms.LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            api_key = UserClient.post_login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                flash('Welcome back, ' + user['result']['username'], 'success')
                return redirect(url_for('frontend.home'))
            else:
                flash('Cannot login', 'error')
        else:
            flash('Errors found', 'error')
    return render_template('login/index.html', form=form)


@frontend_blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('frontend.login'))


@frontend_blueprint.route('/product/<id>', methods=['GET'])
def product(id):
    response = SatelliteClient.get_satellite(id)
    item = response['result']
    if request.method == "POST":
        if 'user' not in session:
            flash('Please login', 'error')
            return redirect(url_for('frontend.login'))
    SatelliteClient.update_satellite_healthy(id=id, json={'healthy': 1})
    SatelliteClient.update_satellite_location(id=id, json={'location': 'east'})
    return render_template('product/index.html', product=item)

@frontend_blueprint.route('/create', methods=['GET','POST'])
def add():
    form = forms.SatForm(request.form)
    if request.method == "POST":
        user = SatelliteClient.add_satellite(form)
        if user:
            flash('Added', 'success')
            return redirect(url_for('frontend.home'))
        else:
            flash('Errors found', 'error')
    return render_template('admin/index.html', form=form)

@frontend_blueprint.route('/product/delete/<id>', methods=['DELETE'])
def delete(id):
    response = SatelliteClient.delete_satellite(id)
    if response:
        return redirect(url_for('frontend.home'))
