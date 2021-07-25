from exts import db
import datetime

class User(db.Model):
    userid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),nullable=False)
    userpassword = db.Column(db.String(64),nullable=False)
    phone = db.Column(db.String(15),nullable=False)
    isdelete = db.Column(db.Boolean,default=False)
    registdatetime = db.Column(db.DateTime,default=datetime.datetime.now)
