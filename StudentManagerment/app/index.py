from app import app, controller, dao
from flask import session, request, render_template, redirect, url_for
import math

app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/login', 'login', controller.login, methods=['get', 'post'])


# app.add_url_rule('/input_student','input_student', controller.input_student,methods=['get','post'])
# app.add_url_rule('/list_student','list_student', controller.list_student(),methods=['get','post'])


@app.route('/list_student')
def list_student():
    kw = request.args.get("keyword")
    page = request.args.get("page", 1)
    student = dao.list_student(kw=kw, page=int(page))  # B1: Lấy student, read load studet lên / Biến student thực hiện trong utils hàm load_student
    counter = dao.count_student()
    return render_template('list_student.html', student=student, pages=math.ceil(counter / app.config["PAGE_SIZE"]))


@app.route("/list_student/<int:student_id>")
def student_detail(student_id):
    student = dao.profile_student(student_id)  # Truyền student_id
    return render_template('info_student.html', student=student)


@app.route("/list_student/input_student", methods=["get", "post"])
def input_student():
    err_msg = ""
    if request.method.lower() == "post":
        full_name = request.form.get("full_name")
        gender = request.form.get("gender")
        birthday = request.form.get("birthday")
        phone = request.form.get("phone")
        email = request.form.get("email")
        if dao.ktra(int(birthday)):
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


@app.route("/list_class")
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


@app.route("/list_class/add_class", methods=["get", "post"])
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


@app.route("/class_detail/<int:class_room_id>")
def class_detail(class_room_id):
    err_msg = ""
    classroom = dao.profile_class(class_room_id)
    student_classroom = dao.read_student_class(class_room_id)
    quantity = dao.count_student_class(class_room_id)
    return render_template('info_class.html', classroom=classroom, student_classroom=student_classroom,
                           quantity=quantity, err_msg=err_msg)


@app.route("/list_class/add_student_class/<int:class_room_id>", methods=["get", "post"])
def add_student_class(class_room_id):
    classroom = dao.profile_class(class_room_id)
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
    return render_template('add_student_class.html', classroom=classroom, err_msg=err_msg)


from app import app, controller, dao, login
from app.admin import *

app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/logout', 'logout', controller.logout_my_user)
app.add_url_rule('/employee', 'employee', controller.index_employee)
app.add_url_rule('/employee/students', 'employee-students', controller.student_employee)
app.add_url_rule('/employee/student/add', 'employee-student-add', controller.employee_student_add)
app.add_url_rule('/login', 'login', controller.user_login, methods=['get', 'post'])


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
