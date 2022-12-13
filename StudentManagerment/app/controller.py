from flask import render_template, request, redirect, url_for
from app import dao
from flask_login import login_user, logout_user, current_user
from models import UserRole


def index():
    return render_template('index.html')


def user_login():
    error_message = ''
    if request.method.__eq__('POST'):
        user = dao.auth_user(username=request.form.get('username'),
                             password=request.form.get('password'))
        if user:
            login_user(user=user)
            # u = request.args.get('next')
            # return redirect(u if u else '/')
            # return render_template('login.html')
            if user.user_role == UserRole.ADMIN:
                return redirect('/admin')
            else:
                return redirect(url_for('index'))
        else:
            error_message = 'Username hoặc mật khẩu chưa đúng!!!'
    return render_template('login.html',error_message = error_message)


def logout_my_user():
    logout_user()
    return redirect('/login')


def student_employee():
    students = dao.load_student()
    return render_template('employee/emp_student.html', students=students)


def index_employee():
    if current_user.is_authenticated and current_user.user_role == UserRole.EMPLOYEE:
        return render_template('employee/emp_index.html')
    else:
        return redirect('/login')


def employee_student_add():
    return render_template('employee/emp_student_add.html')
