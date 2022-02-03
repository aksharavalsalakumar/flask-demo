from flask_restful import Resource,reqparse
from Model.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help='username cant be empty'
    )
    parser.add_argument('password',
    type=str,
    required=True,
    help='password cant be empty'
    )
    def post(self):
        data=UserRegister.parser.parse_args()
        user=UserModel.find_by_name(data["username"])
        if user:
            return {'message':'user with username {} already exist'.format(data['username'])}
        user=UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message":"user registered successfully"}