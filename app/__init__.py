from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_admin import  Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "Q\xcd&3XO\x00S \xc9\x9c\xfc\x96\xd3q\xaf\x8d"
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:123456@localhost/qlphongve?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app,name="Quan Ly Ban Ve May Bay", template_mode="bootstrap3")

login = LoginManager(app=app)