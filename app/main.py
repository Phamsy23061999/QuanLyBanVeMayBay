from flask import render_template, redirect, request,session
from flask_login import login_user, login_required

from app import app, login, dao
from app.dao import read_chuyenbay
from app.models import *
import hashlib

@app.route("/")

def index():
    form = Form()
    form.San_Bay_Di.choices = [(San_Bay_Di.San_Bay_Di) for San_Bay_Di in ChuyenBay.query.all()]
    form.San_Bay_Den.choices = [(San_Bay_Den.San_Bay_Den) for San_Bay_Den in ChuyenBay.query.all()]
    print(form.San_Bay_Di.choices)
    print(len(form.San_Bay_Di.choices))
    return render_template("index.html", form = form, cacchuyenbay=form.San_Bay_Di.choices, len = len(form.San_Bay_Di.choices))

@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method =='POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = Admin.query.filter(Admin.username == username.strip(),
                                 Admin.password == password).first()
        if user:
            if user.active== 1:
                login_user(user=user)
            if user.active== 0:
                return render_template("index.html")

    return redirect("/admin")

@app.route("/search", methods=['GET', 'POST'] )
def search():
    San_Bay_Di = request.form['San_Bay_Di']
    San_Bay_Den = request.form['San_Bay_Den']
    # San_Bay_Den = request.form['San_Bay_Den'],San_Bay_Den=San_Bay_Den
    return render_template("Search.html", chuyenbay = dao.read_chuyenbay(San_Bay_Di=San_Bay_Di, San_Bay_Den=San_Bay_Den))





@login.user_loader
def user_load(user_id):
    return Admin.query.get(user_id)



@app.route("/templates/contact")
def ChuyenTrangContact():
    return render_template("contact.html")

@app.route("/logout")
def logout():
    session["user"]=None
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)

