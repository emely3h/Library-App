from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user
from app.authentication.helpers.forms import LoginForm, RegistrationForm
from app.authentication.models import User


blueprint = Blueprint('authentication', __name__)


@blueprint.route("/", methods=['GET'])
def home():
    all_users = User.query.all()
    return render_template('index.html', users = all_users)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('entered login route')
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('.home'))
        login_user(user)
        return redirect(url_for('.home')) 
    return render_template('authentication/login.html', form=form)

@blueprint.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        login_user(user)
        return redirect(url_for('.home'))
    return render_template('authentication/registration.html', form=form)
        
@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.home'))





