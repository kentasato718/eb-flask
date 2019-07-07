from app import application
from flask import render_template, redirect, url_for
from app.forms import SignUpForm


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        print(
            form.name.data,
            form.email.data,
            form.mobile.data,
            form.country.data,
            form.newsletter.data
            )
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)