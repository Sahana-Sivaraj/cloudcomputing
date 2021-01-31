FROM python:3.8
COPY requirements.txt /satapp/requirements.txt
WORKDIR /satapp
RUN pip install -U flask-cors
RUN pip install -U flask_script
RUN pip install -r requirements.txt
COPY . /satapp
ENTRYPOINT ["python"]
CMD ["run.py"]