from app import app, controller, dao, login
from flask import session, request, render_template, redirect, url_for
import math

app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/login', 'login', controller.login, methods=['get', 'post'])

# app.add_url_rule('/input_student','input_student', controller.input_student,methods=['get','post'])
# app.add_url_rule('/list_student','list_student', controller.list_student(),methods=['get','post'])

# Block base
app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/logout', 'logout', controller.logout_my_user)
app.add_url_rule('/login', 'login', controller.user_login, methods=['get', 'post'])
# Endblock base

# Block employee
app.add_url_rule('/employee', 'employee', controller.emp_index)
app.add_url_rule('/employee/students', 'employee-students', controller.emp_load_student)
app.add_url_rule('/employee/student/add', 'employee-student-add', controller.emp_add_student, methods=['GET', 'POST'])
app.add_url_rule('/employee/classes', 'classes', controller.emp_load_class)
# Endblock employee


# app.add_url_rule('/list_student', 'list-student', controller.list_student)
app.add_url_rule('/list_student/<int:student_id>', 'student-detail', controller.student_detail)


# app.add_url_rule('/list_student/input_student', 'add-student', controller.input_student, methods=['get', 'post'])
# app.add_url_rule('/list_class', 'list-class', controller.list_class)
# app.add_url_rule('/list_class/add_class', 'add-class', controller.add_class, methods=['get', 'post'])
# app.add_url_rule('/class_detail/<int:class_room_id>', 'class-detail', controller.class_detail)
# app.add_url_rule('/list_class/add_student_class/<int:class_room_id>', 'add-student-class', controller.add_student_class,
#                  methods=['get', 'post'])
# app.add_url_rule('/list_subject', 'list-subject', controller.list_subject)
# app.add_url_rule('/list_subject/add_subject', 'add-subject', controller.add_subject, methods=['get', 'post'])


@app.route('/list_student')
def list_student():
    kw = request.args.get("keyword")
    page = request.args.get("page", 1)
    student = dao.list_student(kw=kw, page=int(
        page))  # B1: L???y student, read load studet l??n / Bi???n student th???c hi???n trong utils h??m load_student
    counter = dao.count_student()
    return render_template('list_student.html', student=student, pages=math.ceil(counter / app.config["PAGE_SIZE"]))


@app.route("/list_student/<int:student_id>")
def student_detail(student_id):
    student = dao.profile_student(student_id)  # Truy???n student_id
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
                err_msg = "H??? th???ng ??ang g???p l???i: " + str(ex)
        else:
            err_msg = "N??m sinh c???a h???c sinh kh??ng ????? quy ?????nh"
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
            err_msg = "H??? th???ng ??ang c?? l???i: " + str(ex)

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
                err_msg = "H??? th???ng ??ang g???p l???i: " + str(ex)
        else:
            err_msg = "S??? l?????ng h???c sinh trong l???p ???? ?????"
    return render_template('add_student_class.html', classroom=classroom, err_msg=err_msg)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
