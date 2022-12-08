import hashlib
from app.models import User
from app import app


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()


if __name__ == '__main__':
    with app.app_context():
        print(auth_user('haianh', '123456').degree)
