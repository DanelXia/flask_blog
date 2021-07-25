from flask_sqlalchemy import SQLAlchemy
from flask import g,redirect
db = SQLAlchemy()

def check_login_wrapper(func):
    def check_login(*args,**kwargs):
        if not g.username:
            return redirect("/index")
        else:
            return func(*args, **kwargs)
    return check_login