import pymongo
from threading import *
from time import *

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["Thread"]
mycol = mydb["Thread-db"]
xg = "global"
yg = "global"


class A(Thread):
    def set(self,x,y):
        self.x=x
        self.y=y

    def run(self):
        mydata = {"name": self.x, "email": self.y}
        global xg, yg
        xg = self.x
        yg = self.y
        insertdata = mycol.insert_one(mydata)
        print(insertdata.inserted_id, "is your id for insert data")


class B(Thread):
    def set(self, p, q):
        self.p = p
        self.q = q

    def run(self):
        global xg, yg
        qeury1 = {"name": xg, "email": yg}
        qeury2 = {"$set": {"name": self.p, "email": self.q}}
        updatevalue = mycol.update_one(qeury1, qeury2)
        print(updatevalue.modified_count, "is Modified")


obja = A()
objb = B()

x = input("Enter Your Name :- ")
y = input("Enter Your Email :- ")
obja.set(x,y)
obja.start()
sleep(0.5)
p = input("Enter Your Name for Update :- ")
q = input("Enter Your Email for Update :- ")
objb.set(p,q)
objb.start()

obja.join()
objb.join()
print("operation complate")