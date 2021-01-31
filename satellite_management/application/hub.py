from application.models import Product, Base
import random
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import config
import threading

conn_string = config.ProductionConfig.SQLALCHEMY_DATABASE_URI
engine = create_engine(conn_string)
Base.metadata.create_all(engine)  # here we create all tables
Session = sessionmaker(bind=engine)
session = Session()

def execute_adding_data():
    # print("here")
    start = datetime.now()
    print("Started at", start)
    student_count = Product.query.count()
    if student_count > 0:
        print('yes',student_count)
    else:
        new_student = Product(name='ABC',location='east',healthy=1)
        new_student1 = Product(name='ABC2', location='west', healthy=1)
        new_student2 = Product(name='ABC3', location='north', healthy=1)
        subjects=[new_student,new_student2,new_student1]
        print('students_added')
        for subject in subjects:
            subject.add()
        print('subjects added')
        print('over')
        ended = datetime.now()
        print('Ended at', ended)

        print('Total time taken', ended - start)