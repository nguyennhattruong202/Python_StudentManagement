from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = '$#&*&%$(*&^(*^*&%^%$#^%&^%*&56547648764%$#^%$&^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/quanlyhocsinh?charset=utf8mb4' % quote(
    '123456789')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["PAGE_SIZE"] = 10

db = SQLAlchemy(app=app)
db = SQLAlchemy(app=app)
login = LoginManager(app=app)
babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return 'vi'
