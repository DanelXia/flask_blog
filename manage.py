from apps import create_app
from exts import db
from model.blog_model import User
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask import request,session,redirect,url_for,render_template,g
app = create_app()

@app.before_request
def get_session():
    g.username = None
    if request.path == "/index":
        return None
    if session.get("username"):
        g.username = session.get("username")



@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/index")
@app.route("/index")
def index():
    return render_template('index.html', childpage="index")

# @app.route("/test")
# @check_login_wrapper
# def test():
#     return "1"

manager = Manager(app)

migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
