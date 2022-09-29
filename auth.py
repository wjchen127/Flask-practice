from flask import render_template, request, Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        content = request.get_json()
        return content
    return render_template('login.html')