from datetime import datetime
from symbol import return_stmt
from tkinter.messagebox import Message
from Tools.scripts.make_ctype import method
from flask import render_template, redirect, request,session,url_for,jsonify
from flask_login import login_user, login_required
from mysql import connector
from flask_mail import Message
from flask_googlecharts import BarChart
from app import mail


from app import app, login, dao, charts
from app.dao import read_chuyenbay
from app.models import *
import hashlib

from app.models import Ve

<<<<<<< HEAD

=======
>>>>>>> f43206efecf8ad49644a8fcfe1b0221b167e2bea
@app.route("/")
def index():
    form = Form()
    form.San_Bay_Di.choices = [(San_Bay_Di.San_Bay_Di) for San_Bay_Di in ChuyenBay.query.all()]
    form.San_Bay_Den.choices = [(San_Bay_Den.San_Bay_Den) for San_Bay_Den in ChuyenBay.query.all()]

    return render_template("index.html", form = form, cacchuyenbay1= form.San_Bay_Di.choices, cacchuyenbay2 = form.San_Bay_Den.choices,
                           len1 = len(form.San_Bay_Di.choices), len2=len(form.San_Bay_Den.choices),
                           latest_products = dao.read_ChuyenBay_show(latest=True))


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
                return redirect(url_for('orderDetail'))

    return redirect("/admin")


<<<<<<< HEAD



=======
>>>>>>> f43206efecf8ad49644a8fcfe1b0221b167e2bea
@app.route("/search", methods=['GET', 'POST'] )
def search():
    if request.method == 'POST' and 'Ngay_Bay' in request.form:
        San_Bay_Di = request.form['San_Bay_Di']
        San_Bay_Den = request.form['San_Bay_Den']
        Ngay_Bay = request.form['Ngay_Bay']

        tim = "%{}%".format(Ngay_Bay)
        session["San_Bay_Di"] = San_Bay_Di
        session["San_Bay_Den"]= San_Bay_Den
        session["Ngay_Bay"] =  Ngay_Bay


        Chuyen_bay = ChuyenBay.query.filter(ChuyenBay.Ngay_Bay.like(tim))

        return render_template("Search.html",chuyenbay = dao.read_chuyenbay(San_Bay_Di=San_Bay_Di,San_Bay_Den=San_Bay_Den),Chuyen_bay=Chuyen_bay)


@login.user_loader
def user_load(user_id):
    return Admin.query.get(user_id)


@app.route("/templates/customer",methods=['GET', 'POST'] )
def info():

        if "San_Bay_Di" and "San_Bay_Den"  in session:

            id = request.form["id"]
            session["id"] = id

            So_Luong_Ghe_Loai_1 = request.form["So_Luong_Ghe_Loai_1"]
            if( int(So_Luong_Ghe_Loai_1) <= 0):
                return jsonify(
                    message = ("Chuyến Bay Này Hiện Đã Hết Vé! Mời Khách Hàng Chọn Lại Chuyến Bay Khác").encode('utf8')

                )
            else:
                session["So_Luong_Ghe_Loai_1"] = So_Luong_Ghe_Loai_1


            San_Bay_Di = session["San_Bay_Di"]
            San_Bay_Den = session["San_Bay_Den"]
            Ngay_Bay = session["Ngay_Bay"]

            Thoi_Gian_Bay = request.form['Thoi_Gian_Bay']
            session["Thoi_Gian_Bay"] = Thoi_Gian_Bay
            Ngay_Ha_Canh = request.form['Ngay_Ha_Canh']
            session["Ngay_Ha_Canh"] = Ngay_Ha_Canh
            tim = "%{}%".format(Ngay_Ha_Canh)
            thoi_gian = "%{}%".format(Thoi_Gian_Bay)
            Thoi_Gian_Ha = request.form['Thoi_Gian_Ha']
            session["Thoi_Gian_Ha"]=Thoi_Gian_Ha
            thoi_gian_ha = "%{}%".format(Thoi_Gian_Ha)
            Gia_Ve_Loai_1 = request.form['Gia_Ve_Loai_1']
            session["Gia_Ve_Loai_1"] = Gia_Ve_Loai_1

            return render_template("customer_information.html",San_Bay_Di=San_Bay_Di,San_Bay_Den=San_Bay_Den,Gia_Ve_Loai_1=Gia_Ve_Loai_1,Ngay_Bay=Ngay_Bay,Thoi_Gian_Bay=Thoi_Gian_Bay
                                   , Ngay_Ha_Canh = Ngay_Ha_Canh,Thoi_Gian_Ha =Thoi_Gian_Ha,id=id,So_Luong_Ghe_Loai_1=So_Luong_Ghe_Loai_1)

        return render_template("customer_information.html",So_luong_ghe_loai_1=So_luong_ghe_loai_1)


@app.route("/order", methods=['GET', 'POST'] )
def orderDetail():

    q=PhieuDatCho.query.all()
    return render_template("OrderDetail.html",q=q)


@app.route("/ve", methods=['GET', 'POST'] )
def insertVe():
    if request.method =='POST':
        Ma_Phieu_Dat_Cho_id = request.form['Ma_Phieu_Dat_Cho_id']
        Gia_Tien = request.form['Gia_Tien']

        Thoi_Gian_Dat_ve = request.form['Thoi_Gian_Dat_ve']

        Tinh_Trang_Da_Thanh_Toan = request.form['Tinh_Trang_Da_Thanh_Toan']

        if Tinh_Trang_Da_Thanh_Toan == '1':
            k = Ve(
                Ma_Phieu_Dat_Cho_id = Ma_Phieu_Dat_Cho_id,
                Thoi_Gian_Dat_ve = Thoi_Gian_Dat_ve,
                Gia_Tien = Gia_Tien,
            )
            db.session.add(k)
            db.session.commit()
        return render_template("Ve.html",k=k)


    return render_template("Ve.html",)


@app.route('/insert', methods=['GET','Post'])
def insert():


     id = session["id"]
     So_Luong_Ghe_Loai_1 = session["So_Luong_Ghe_Loai_1"]

     San_Bay_Di = session["San_Bay_Di"]
     San_Bay_Den = session["San_Bay_Den"]
     Ngay_Bay = session["Ngay_Bay"]
     Thoi_Gian_Bay = session["Thoi_Gian_Bay"]
     Ngay_Ha_Canh = session["Ngay_Ha_Canh"]
     Thoi_Gian_Ha = session["Thoi_Gian_Ha"]
     Gia_Ve_Loai_1 = session["Gia_Ve_Loai_1"]



     Quy_Danh = request.form['Quy_Danh']
     Ten_Khach_Hang = request.form['Ten_Khach_Hang']
     Dia_Chi = request.form['Dia_Chi']
     CMND = request.form['CMND']
     Email = request.form['Email']
     SDT = request.form['SDT']
     Ghi_Chu = request.form['Ghi_Chu']
<<<<<<< HEAD
     p = KhachHang(
         Quy_Danh=Quy_Danh, Ten_Khach_Hang=Ten_Khach_Hang, Dia_Chi=Dia_Chi, CMND=CMND, Email=Email, SDT=SDT,
         Ghi_Chu=Ghi_Chu
     )
     db.session.add(p)
     db.session.commit()



     Chuyen_Bay = ChuyenBay.query.filter_by(id=id).update(dict(So_Luong_Ghe_Loai_1=(int(So_Luong_Ghe_Loai_1) - 1)))
     db.session.commit()



     q = PhieuDatCho(
         Khach_Hang_id=p.id,
         Ma_Chuyen_Bay_id = session["id"],
         Gia_Tien=session["Gia_Ve_Loai_1"],
         Thoi_Gian_Dat_ve=datetime.now(),
     )
     db.session.add(q)
     db.session.commit()

     Ma_Chuyen_Bay_id = q.id




     if request.method == 'POST':
         msg = Message("Mail Xác Nhận Đơn Hàng", sender="webbanve@gmail.com", recipients=[Email])
         msg.html = render_template('email.html',Ma_Chuyen_Bay_id=Ma_Chuyen_Bay_id, Quy_Danh=Quy_Danh, Ten_Khach_Hang=Ten_Khach_Hang, Dia_Chi=Dia_Chi,
                                    CMND=CMND, Email=Email, SDT=SDT, Ghi_Chu=Ghi_Chu, San_Bay_Di=San_Bay_Di,
                                    San_Bay_Den=San_Bay_Den, Ngay_Bay=Ngay_Bay,
                                    Thoi_Gian_Bay=Thoi_Gian_Bay, Ngay_Ha_Canh=Ngay_Ha_Canh, Thoi_Gian_Ha=Thoi_Gian_Ha,
                                    Gia_Ve_Loai_1=Gia_Ve_Loai_1)
         mail.send(msg)

     return render_template("customer_information.html")




=======
     if request.method == 'POST':
         msg = Message("Email xác nhận", sender="webbanve@gmail.com", recipients=[Email])
         msg.html = render_template('email.html',Quy_Danh=Quy_Danh,Ten_Khach_Hang=Ten_Khach_Hang,Dia_Chi = Dia_Chi,
                                    CMND = CMND,Email = Email,SDT = SDT,Ghi_Chu = Ghi_Chu)
         mail.send(msg)

     return render_template("customer_information.html",info=dao.add_Khachhang(Quy_Danh=Quy_Danh,
                                                                               Ten_Khach_Hang=Ten_Khach_Hang,
                                                                               Dia_Chi = Dia_Chi,CMND = CMND,
                                                                               Email = Email,SDT = SDT,Ghi_Chu = Ghi_Chu))
>>>>>>> f43206efecf8ad49644a8fcfe1b0221b167e2bea


@app.route("/logout")
def logout():
    session["user"]=None
    return render_template("index.html")

<<<<<<< HEAD
=======

@app.route("/simple_chart", methods=['GET','Post'] )
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('admin/abous-us.html', values=values, labels=labels, legend=legend)


@app.route("/thanhtoan")
def payurl():

    return render_template("testmomo.html", res=dao.payment_momo())

>>>>>>> f43206efecf8ad49644a8fcfe1b0221b167e2bea

if __name__=="__main__":
    app.run(debug=True)

