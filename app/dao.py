from tokenize import String

from app import app
import os

from app.models import ChuyenBay


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
            print(San_Bay_Di ==  chuyenbay[i].San_Bay_Di.Ten_San_Bay)
            print(chuyenbay[i].San_Bay_Den)
            if(San_Bay_Di ==  chuyenbay[i].San_Bay_Di.Ten_San_Bay and San_Bay_Den ==  chuyenbay[i].San_Bay_Den.Ten_San_Bay ):
                cacchuyenbay.append(chuyenbay[i])
    print("cac chuyen bay: ", cacchuyenbay)

    return cacchuyenbay[0]

if __name__ == "__main__":
    print(read_chuyenBay())