from flask import Blueprint,render_template,request,redirect,url_for,session,g
blog_bp = Blueprint('blog',__name__,url_prefix='/blog')
from model.blog_model import User
from exts import db
from exts import check_login_wrapper
@blog_bp.route("/")
def show_index():
    return render_template('index.html',childpage="index")


@blog_bp.route("/show_login")
def show_login():
        return render_template("login.html")


@blog_bp.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user:
            if pwd == user.userpassword:
                session["username"] = user.username
                g.username = session["username"]
                return render_template("index.html",childpage="index")
    else:
        return redirect("/blog/show_login")


@blog_bp.route("/register",endpoint='register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('userpassword1')
        password2 = request.form.get('userpassword2')
        phonenumber = request.form.get('phonenumber')
        if password1 == password2:
            #注册进表
            user = User()
            user.username = username
            user.userpassword = password1
            user.phone = phonenumber
            db.session.add(user)
            db.session.commit()
            return '注册成功'
        else:
            return '重复确认密码不对'
    else:
        return render_template("register.html")


@blog_bp.route("/userall",endpoint="userall")
@check_login_wrapper
def userall():
    users = User.query.filter_by(isdelete=False).all()
    number = User.query.filter_by(isdelete=False).count()
    return render_template("userall.html",users=users,childpage="userall",number=number)


@blog_bp.route("/del/<int:userid>")
@check_login_wrapper
def deluser(userid):
    user = User.query.filter_by(userid=userid).first()
    user.isdelete = True
    db.session.commit()
    return redirect(url_for("blog.userall"))

@blog_bp.route("/show_update/<int:userid>",endpoint="show_update")
@check_login_wrapper
def show_update(userid):
    user = User.query.filter_by(userid=userid).first()
    return render_template("register.html",user=user)