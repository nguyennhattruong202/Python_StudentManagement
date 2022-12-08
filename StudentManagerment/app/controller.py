from flask import render_template, request, redirect
from app import dao
from flask_login import login_user


def index():
    return render_template('index.html')


def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            u = request.args.get('next')
            return redirect(u if u else '/')
    return render_template('login.html')
