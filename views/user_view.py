from flask import blueprints,Blueprint,g,session,request

user_bp = Blueprint('user',__name__,url_prefix='/user')

# from manage import app
#
# @app.before_first_request
# def getsession():
#     if request.path == "/blog":
#         return None
