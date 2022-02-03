from flask import render_template
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from Model.employees import EmployeeModel


# class EmployeesList(Resource):
#     def get(self):
#         employees=[emp.json() for emp in EmployeeModel.query.all()]
#         return {"employees":employees}


class EmployeesList(Resource):
    def get(self):
        return render_template('details.html')

# class EmployeesList(Resource):
#     def get(self):
#         employees=[emp.json() for emp in EmployeeModel.query.all()]
#         return {"employees":employees}

class Employees(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name',
    type=str,
    required=True,
    help='name cant be empty'
    )
    parser.add_argument('age',
    type=int,
    required=True,
    help='age cant be empty'
    )
    parser.add_argument('salary',
    type=int,
    required=True,
    help='salary cant be empty'
    )
    parser.add_argument('designation',
    type=str,
    required=True,
    help='designation cant be empty'
    )
    def post(self):
        data=Employees.parser.parse_args()
        emp=EmployeeModel.find_by_name(data['name'])
        if emp:
            return {'message':'employee with name {} already exist'.format(data['name'])}
        emp=EmployeeModel(data['name'],data['age'],data['salary'],data['designation'])
        emp.save_to_db()
        return {"message":"employee added successfully"}
