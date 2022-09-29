# -*- coding: utf-8 -*-
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

from main import main as main_blueprint
app.register_blueprint(main_blueprint)
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def exception_handler(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
        

