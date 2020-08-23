from flask import render_template, redirect, request,session
from flask_login import login_user, login_required
from app import app, login
from app.models import *
import hashlib

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method =='POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = Admin.query.filter(Admin.username == username.strip(),
                                 Admin.password == password).first()
        if user:
            if( Admin.active == 0):
                return render_template("index.html")
            else:
                login_user(user=user)
    return redirect("/admin")


@login.user_loader
def user_load(user_id):
    return Admin.query.get(user_id)



@app.route("/templates/contact")
def ChuyenTrangContact():
    return render_template("contact.html")




if __name__=="__main__":
    app.run(debug=True)

