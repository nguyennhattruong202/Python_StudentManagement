from app import app, db
from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from app.models import Student, User, UserRole, ClassRoom, Grade, Semester, Subject, ScoreType, TeachDetail, Score
from flask_login import current_user, logout_user
from flask import redirect, url_for


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect(url_for('login'))


class UserModelView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['id', 'full_name', 'birthday', 'phone', 'email', 'identity']
    column_filters = ['full_name', 'gender', 'phone', 'email', 'identity', 'degree', 'position']
    column_exclude_list = ['username', 'password', 'user_role']
    column_labels = {
        'full_name': 'Họ và tên',
        'gender': 'Giới tính',
        'birthday': 'Ngày sinh',
        'identity': 'CCCD/CMND',
        'degree': 'Học vị',
        'position': 'Chức vụ'
    }


class StudentModelView(AuthenticatedModelView):
    can_view_details = True


class ClassRoomModelView(AuthenticatedModelView):
    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'name': 'Lớp',
        'max_quantity': 'Sĩ số tối đa'
    }
    form_excluded_columns = ['students']


class GradeModelView(AuthenticatedModelView):
    column_display_pk = True


class SemesterModelView(AuthenticatedModelView):
    column_display_pk = True


class SubjectModelView(AuthenticatedModelView):
    column_display_pk = True


class ScoreTypeModelView(AuthenticatedModelView):
    column_display_pk = True


class TeachDetailModelView(AuthenticatedModelView):
    column_display_pk = True


class ScoreModelView(AuthenticatedModelView):
    column_display_pk = True


class AdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/home.html')


admin = Admin(app=app, name='E-SM', template_mode='bootstrap4', index_view=AdminView)
admin.add_view(StudentModelView(Student, db.session, name="Học sinh"))
admin.add_view(UserModelView(User, db.session, name='Người dùng'))
admin.add_view(ClassRoomModelView(ClassRoom, db.session, name='Lớp'))
admin.add_view(GradeModelView(Grade, db.session, name='Khối lớp'))
admin.add_view(SemesterModelView(Semester, db.session, name='Khóa học'))
admin.add_view(SubjectModelView(Subject, db.session, name='Môn học'))
admin.add_view(ScoreTypeModelView(ScoreType, db.session, name='Loại điểm'))
admin.add_view(TeachDetailModelView(TeachDetail, db.session, name='Giảng dạy'))
admin.add_view(ScoreModelView(Score, db.session, category='Điểm số'))
admin.add_view(LogoutView(name="Đăng xuất"))
