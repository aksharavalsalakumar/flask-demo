from flask import Flask, redirect, render_template, request, url_for
from flask_restful import Api
from flask_jwt import JWT
from Resources.employees import Employees, EmployeesList
from Resources.user import UserRegister
from db import db
from Model.employees import EmployeeModel
from security import authenticate, identity

app=Flask(__name__)
app.secret_key='akshara'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)

# api.add_resource(UserRegister,'/register')
# api.add_resource(EmployeesList,'/employeeslist')
# api.add_resource(Employees,'/employees')

@app.route('/home')
def home():
    all_data = EmployeeModel.query.all()
    return render_template("details.html", employees = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        designation = request.form['designation']

        my_data = EmployeeModel(name, age, salary,designation)
        db.session.add(my_data)
        db.session.commit()
 
        # flash("Employee Inserted Successfully")

        return redirect(url_for('home'))
 
 
#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = EmployeeModel.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.age = request.form['age']
        my_data.salary = request.form['salary']
        my_data.designation = request.form['designation']
 
        db.session.commit()
        # flash("Employee Updated Successfully")
 
        return redirect(url_for('home'))
 
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = EmployeeModel.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Employee Deleted Successfully")
 
    return redirect(url_for('home'))

if __name__ =='__main__':
    db.init_app(app)
    app.run(port=4000,debug=True)