from app import application
from flask import render_template


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')
