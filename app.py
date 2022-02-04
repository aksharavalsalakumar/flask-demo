from flask import Flask, redirect, render_template, request, url_for
from flask_restful import Api
from flask_jwt import JWT
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

@app.route('/home')
def home():
    employee_list = EmployeeModel.query.all()
    return render_template("details.html", employees = employee_list)
 
 
@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        designation = request.form['designation']
        new_data = EmployeeModel(name, age, salary,designation)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('home'))
 
@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    if request.method == 'POST':
        new_data = EmployeeModel.query.get(request.form.get('id'))
        new_data.name = request.form['name']
        new_data.age = request.form['age']
        new_data.salary = request.form['salary']
        new_data.designation = request.form['designation']
        db.session.commit()
        return redirect(url_for('home'))
 
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    new_data = EmployeeModel.query.get(id)
    db.session.delete(new_data)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ =='__main__':
    db.init_app(app)
    app.run(port=4000,debug=True)