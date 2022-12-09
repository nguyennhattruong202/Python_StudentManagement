from flask import render_template, request, redirect, url_for
from app import dao
from flask_login import login_user, logout_user
from app.models import UserRole


def index():
    return render_template('index.html')


def user_login():
    error_message = ''
    if request.method.__eq__('POST'):
        user = dao.auth_user(username=request.form.get('username'), password=request.form.get('password'))
        if user:
            login_user(user=user)
            if user.user_role == UserRole.ADMIN:
                return redirect('/admin')
            else:
                return redirect(url_for('index'))
        else:
            error_message = 'Username hoặc password không chính xác'
    return render_template('login.html', error_message=error_message)


def logout_my_user():
    logout_user()
    return redirect('/login')
