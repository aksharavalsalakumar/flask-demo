from flask_restful import Resource
from db import db

class EmployeeModel(db.Model):
    __tablename__='employees'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)
    salary=db.Column(db.Integer)
    designation=db.Column(db.String(80))

    def __init__(self,name,age,salary,designation):
        self.name=name
        self.age=age
        self.salary=salary
        self.designation=designation

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
