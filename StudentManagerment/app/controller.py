from flask import render_template, request, redirect, url_for
from app import dao, app
from flask_login import login_user, logout_user, current_user
from models import UserRole
import math


def add_subject():
    list_grade = dao.list_grade()
    err_msg = ""
    if request.method.lower() == "post":
        subject = request.form.get("subject")
        try:
            dao.add_subject(subject)
            return redirect(url_for("list_subject"))
        except Exception as ex:
            err_msg = "Hệ thống đang có lỗi: " + str(ex)

    return render_template('add_subject.html', list_grade=list_grade, err_msg=err_msg)


def list_subject():
    kw_grade = request.args.get("grade")
    kw_subject = request.args.get("subject")
    # listsubject = dao.list_subject(kw_grade, kw_subject)
    list_grade = dao.list_grade()
    listsubject = dao.list_subject()
    return render_template('list_subject.html', listsubject=listsubject, list_grade=list_grade)


def add_student_class(class_room_id):
    class_room = dao.profile_class(class_room_id)
    err_msg = ""
    if request.method.lower() == "post":
        full_name = request.form.get("full_name")
        gender = request.form.get("gender")
        birthday = request.form.get("birthday")
        phone = request.form.get("phone")
        email = request.form.get("email")
        class_room_id = int(class_room_id)
        if dao.count_quantity(int(class_room_id)):
            try:
                dao.add_student_class(full_name=full_name, gender=gender, birthday=birthday, phone=phone,
                                      email=email, class_room_id=class_room_id)
                return redirect(url_for("class_detail", class_room_id=class_room_id))
            except Exception as ex:
                err_msg = "Hệ thống đang gặp lỗi: " + str(ex)
        else:
            err_msg = "Số lượng học sinh trong lớp đã đủ"
    return render_template('add_student_class.html', class_room=class_room, err_msg=err_msg)


def add_student_class(class_room_id):
    class_room = dao.profile_class(class_room_id)
    err_msg = ""
    if request.method.lower() == "post":
        full_name = request.form.get("full_name")
        gender = request.form.get("gender")
        birthday = request.form.get("birthday")
        phone = request.form.get("phone")
        email = request.form.get("email")
        class_room_id = int(class_room_id)
        if dao.count_quantity(int(class_room_id)):
            try:
                dao.add_student_class(full_name=full_name, gender=gender, birthday=birthday, phone=phone,
                                      email=email, class_room_id=class_room_id)
                return redirect(url_for("class_detail", class_room_id=class_room_id))
            except Exception as ex:
                err_msg = "Hệ thống đang gặp lỗi: " + str(ex)
        else:
            err_msg = "Số lượng học sinh trong lớp đã đủ"
    return render_template('add_student_class.html', class_room=class_room, err_msg=err_msg)


def class_detail(class_room_id):
    err_msg = ""
    class_room = dao.profile_class(class_room_id)
    student_classroom = dao.read_student_class(class_room_id)
    quantity = dao.count_student_class(class_room_id)
    return render_template('info_class.html', class_room=class_room, student_classroom=student_classroom,
                           quantity=quantity, err_msg=err_msg)


def add_class():
    list_grade = dao.list_grade()
    err_msg = ""
    if request.method.lower() == "post":
        class_room_id = request.form.get("class_room_id")
        name = request.form.get("classroom")
        try:
            dao.add_class(class_room_id=class_room_id, name=name)
            return redirect(url_for("list_class"))
        except Exception as ex:
            err_msg = "Hệ thống đang có lỗi: " + str(ex)
    return render_template('add_class.html', list_grade=list_grade, err_msg=err_msg)


def list_class():
    page = request.args.get("page", 1)
    counter = dao.count_class()

    kw_grade = request.args.get("grade")
    kw_class = request.args.get("class_room")
    grade = dao.list_grade()
    classroom = dao.list_class()
    classroom_quantity = dao.read_classroom_quantity(kw_grade=kw_grade, kw_class=kw_class, page=int(page))
    return render_template('list_class.html', grade=grade, classroom=classroom, classroom_quantity=classroom_quantity,
                           pages=math.ceil(counter / app.config["PAGE_SIZE"]))


def input_student():
    err_msg = ""
    if request.method.lower() == "post":
        full_name = request.form.get("full_name")
        gender = request.form.get("gender")
        birthday = request.form.get("birthday")
        phone = request.form.get("phone")
        email = request.form.get("email")
        if dao.dob(birthday):
            try:
                dao.add_or_update_student(full_name=full_name, gender=gender, birthday=birthday, phone=phone,
                                          email=email)
                return redirect(url_for("list_student"))
            except Exception as ex:
                err_msg = "Hệ thống đang gặp lỗi: " + str(ex)
        else:
            err_msg = "Năm sinh của học sinh không đủ quy định"
    student_id = request.args.get("student_id")
    student = None
    student = dao.profile_student(student_id)
    return render_template('input_student.html', err_msg=err_msg, student=student)


def student_detail(student_id):
    student = dao.profile_student(student_id)  # Truyền student_id
    return render_template('info_student.html',
                           student=student)


# def list_student():
#     kw = request.args.get("keyword")
#     page = request.args.get("page", 1)
#     student = dao.list_student(kw=kw, page=int(page))
#     counter = dao.count_student()
#     return render_template('employee/list_student.html', student=student,
#                            pages=math.ceil(counter / app.config["PAGE_SIZE"]))


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
    return render_template('login.html', error_message=error_message)


def logout_my_user():
    logout_user()
    return redirect('/login')


# Block emp --- nguyennhatruong202
def emp_index():
    if current_user.is_authenticated and current_user.user_role == UserRole.EMPLOYEE:
        return render_template('employee/index.html')
    else:
        return redirect('/login')


def emp_load_student():
    keyword = request.args.get('keyword')
    choose = request.args.get('choose')
    students = dao.load_student(keyword=keyword, choose=choose)
    return render_template('employee/list_student.html', students=students, keyword=keyword)


def emp_load_class():
    keyword = request.args.get('keyword')
    choose = request.args.get('choose')
    classes = dao.load_class(keyword=keyword, choose=choose)
    return render_template('employee/list_class.html', classes=classes)


def emp_add_student():
    message = ''
    classes = dao.load_all_class()
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        birthday = request.form['birthday']
        phone = request.form['phone']
        email = request.form['email']
        class_room_id = request.form['class_room_id']
        student = dao.add_student(full_name=full_name, gender=gender, birthday=birthday, phone=phone, email=email,
                                  class_room_id=int(class_room_id))
        if student:
            message = 'Thêm thành công'
        else:
            message = 'Thêm thất bại'
    return render_template('employee/add_student.html', message=message, classes=classes)
# Endblock emp - nguyennhattruong202
