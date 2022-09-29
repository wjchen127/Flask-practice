# -*- coding: utf-8 -*-
import os
from flask import redirect, url_for, request ,Blueprint, send_from_directory, current_app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

main = Blueprint('main', __name__)

@main.route('/')
def hello():
    return 'Hello, World!'

@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)

@main.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('main.uploaded_file',filename=filename))
    return '''
        <!doctype html>
        <title>Upload Page</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@main.route("/redirect")
def toredirect():
    return redirect(url_for('hello'))
