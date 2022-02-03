from Model.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username,password):
    user=UserModel.find_by_name(username)
    if user and safe_str_cmp(password,user.password):
        return user


def identity(payload):
    user_id=payload['identity']
    user=UserModel.find_by_id(user_id)
    return user