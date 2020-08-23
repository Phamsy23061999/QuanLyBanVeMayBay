from sqlalchemy import Column, Integer, String, Float, DateTime, Time, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db, admin
from flask import render_template
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin,current_user, logout_user
from flask import redirect



class Admin(db.Model, UserMixin):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class KhachHang(db.Model):
    __tablename__ = "khachhang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    TenKhachHang = Column(String(200), nullable=False)
    DiaChi = Column(String(200), nullable=True)
    CMND = Column(Integer, nullable=False)
    Email = Column(String(50), nullable=False)
    SDT = Column(Integer, nullable=False)
    GhiChu = Column(String(50), nullable=False)
    PhieuDatCho = relationship('PhieuDatCho', backref='khachhang', lazy=True)

    def __str__(self):
        return self.TenKhachHang


class SanBay(db.Model):
    __tablename__ = "sanbay"
    id = Column(Integer, primary_key=True, autoincrement=True)
    TenSB = Column(String(100), nullable=True)
    SanBayTrungGian = relationship('SanBayTG', backref='sanbay', lazy=False)
    chuyenbays = db.relationship('ChuyenBay', primaryjoin='or_(SanBay.id==ChuyenBay.SanBayDi_id, SanBay.id==ChuyenBay.SanBayDen_id)',
                              lazy = False) #'dynamic')

    def __str__(self):
        return self.TenSB

class ChuyenBay(db.Model):
    __tablename__ = "chuyenbay"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(100),nullable=False)
    ThoiGianBay = Column(Time, nullable=True)
    SoLuongGheLoai1 = Column(Integer, default= 60, nullable=False)
    SoLuongGheLoai2 = Column(Integer, default= 70,  nullable=False)
    GiaVeLoai1 = Column(Float, nullable=False)
    GiaVeLoai2 = Column(Float, nullable=False)
    PhieuDatCho_id = relationship('PhieuDatCho', backref='chuyenbay', lazy=True)
    SanBayTG_id = relationship('SanBayTG', backref='chuyenbay', lazy=True)

    SanBayDi_id = Column(Integer, ForeignKey('sanbay.id'), nullable=False)
    SanBayDen_id = Column(Integer, ForeignKey('sanbay.id'), nullable=False)

    SanBayDi = db.relationship('SanBay', foreign_keys='ChuyenBay.SanBayDi_id')
    SanBayDen = db.relationship('SanBay', foreign_keys='ChuyenBay.SanBayDen_id')

    def __str__(self):
        return self.name

class PhieuDatCho(db.Model):
    __tablename__ = "phieudatcho"
    id = Column(Integer, primary_key=True, autoincrement=True)
    KhachHang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    MaChuyenBay_id = Column(Integer, ForeignKey(ChuyenBay.id), nullable=False)
    HangVe = Column(String(50), nullable=False)
    GiaTien = Column(Float, nullable=False)
    CoHieuLuc = Column(Boolean, nullable=False)
    Ve_id = relationship('Ve', backref='PhieuDatCho', lazy=True)


class LichSuGiaoDich(db.Model):
    __tablename__ = "lichsugiaodich"
    id = Column(Integer, primary_key=True, autoincrement=True)
    MaChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id), nullable=False)
    NgayBay = Column(DateTime, nullable=True)
    MaPhieuDatCho_id = Column(Integer, ForeignKey(PhieuDatCho.id), nullable=False)


class SanBayTG(db.Model):
    __tablename__ = "sanbayTG"
    id = Column(Integer, primary_key=True, autoincrement=True)
    SanBayId = Column(Integer, ForeignKey(SanBay.id), nullable=False)
    MaChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id), nullable=False)
    ThoiGianDungToiThieu = Column(Time, nullable=False)
    ThoiGianDungToiDa = Column(Time, nullable=False)


class Ve(db.Model):
    __tablename__ = "ve"
    id = Column(Integer, primary_key=True, autoincrement=True)
    MaPhieuDatCho_id = Column(Integer, ForeignKey(PhieuDatCho.id), nullable=False)
    Hangve = Column(String(50), nullable=False)
    GiaTien = Column(Float, nullable=False)

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class SanBayModelView(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    form_columns = ('TenSB',)

class SanBayTGModelView(AuthenticatedView):
       column_display_pk = True
       can_create = True
       can_export = True
       #form_columns = ('SanBayId','ThoiGianDungToiThieu','ThoiGianDungToiDa',)

class ChuyenBayModelView(AuthenticatedView):
    can_create = True
    can_export = True
    form_columns = ('SanBayDi','SanBayDen','name', 'ThoiGianBay','SoLuongGheLoai1','SoLuongGheLoai2','GiaVeLoai1','GiaVeLoai2')

class AboutUsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/about-us.html")

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
         
        logout_user()
        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(SanBayModelView(SanBay, db.session))
admin.add_view(SanBayTGModelView(SanBayTG, db.session))
admin.add_view(ChuyenBayModelView(ChuyenBay, db.session))
admin.add_view(AboutUsView(name="Thống Kê"))
admin.add_view(LogoutView(name="Logout"))
if __name__ == "__main__":
    db.create_all()
