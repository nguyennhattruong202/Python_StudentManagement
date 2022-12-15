from app import app, controller, dao, login

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


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
