from app import application
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
import boto3

db = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = db.Table('signuptable')

@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        table.put_item(
            Item={
                'name': form.name.data,
                'email': form.email.data,
                'mobile': form.mobile.data,
                'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        )
        msg = 'Conguratulations !!! {} is now a Premium Member !'.format(form.name.data)
        flash(msg)
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)