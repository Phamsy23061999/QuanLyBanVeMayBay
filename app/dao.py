from tokenize import String

from app import app, db
import os

from app.models import ChuyenBay, KhachHang


def read_chuyenbay(San_Bay_Di_id=0,San_Bay_Den_id=0,San_Bay_Di=None,San_Bay_Den=None):
    chuyenbay= ChuyenBay.query.filter().all()
    cacchuyenbay = []
    if San_Bay_Di_id > 0:
        chuyenbay = [p for p in chuyenbay if p["San_Bay_Di_id"] == San_Bay_Di_id]
    if San_Bay_Den_id > 0:
        chuyenbay = [p for p in chuyenbay if p["San_Bay_Den_id"] == San_Bay_Den_id]
    if San_Bay_Di and San_Bay_Den:
        chuyenbay = ChuyenBay.query.filter().all()
        for i in range(0, len(chuyenbay)):
            if(San_Bay_Di ==  chuyenbay[i].San_Bay_Di.Ten_San_Bay and San_Bay_Den ==  chuyenbay[i].San_Bay_Den.Ten_San_Bay ):
                cacchuyenbay.append(chuyenbay[i])

        return cacchuyenbay[0]




def add_Khachhang(Quy_Danh = None, Ten_Khach_Hang = None, Dia_Chi = None, CMND =0, Email = None, SDT = 0, Ghi_Chu=None):
    p = KhachHang(
        Quy_Danh = Quy_Danh, Ten_Khach_Hang = Ten_Khach_Hang, Dia_Chi=Dia_Chi, CMND = CMND, Email = Email, SDT= SDT, Ghi_Chu = Ghi_Chu
    )
    db.session.add(p)
    db.session.commit()



def read_ChuyenBay_show(San_Bay_Di_id=0, San_Bay_Den_id=0, San_Bay_Di=None, San_Bay_Den=None, latest=False):
    q=ChuyenBay.query

    if San_Bay_Di:
        q= q.filter(ChuyenBay.name.contains(San_Bay_Di))
    if San_Bay_Den:
        q=q.filter(ChuyenBay.name.contains(San_Bay_Den))
    if latest:
        return q.all()[:5]
    return q.all()

if __name__ == "__main__":
    print(read_chuyenBay())