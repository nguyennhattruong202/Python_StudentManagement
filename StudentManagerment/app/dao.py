import hashlib
import time
import datetime
from models import User,Person,Student,Grade,ClassRoom,Subject,ScoreType,Score
from app import app,db
from sqlalchemy import func
from app import app


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()

def add_or_update_student(full_name, gender, birthday, phone, **kwargs): #kwargs: những thông tin không bắt buộc
    student = Student(full_name=full_name, gender=gender, birthday=birthday, phone=phone, email=kwargs.get('email'))
    db.session.add(student)
    db.session.commit()


def list_student(kw=None, kw_date=None, page=1):
    student = Student.query
    if kw:
        student = student.filter(Student.full_name.contains(kw.lower()))
    if kw_date:
        student = student.filter(Student.birthday.__eq__(kw_date))
    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    end = start + page_size

    return student.slice(start, end).all()

def count_student():
    return Student.query.count()


def profile_student(student_id):
    return Student.query.get(student_id)

# def quy_dinh():
#     return quydinh.query.get(1)



def tinh_tuoi(birthday):
    x = time.localtime().tm_year
    y = datetime.datetime(birthday).year
    a = x - y
    return a


def dob(birthday):
    x = tinh_tuoi(birthday)
    # p = quydinh.query.get(1)
    if x >= 15 and x <= 20:
        return True
    else:
        return False

def list_grade():
    return Grade.query.all()

def list_class(kw_grade=None, kw_class=None, page=1):
    return ClassRoom.query.all()

def profile_class(class_room_id):   #Phương thức
    return ClassRoom.query.get(class_room_id)

def read_student_class(class_room_id): # select field tupple choice
    return Student.query.filter(Student.class_room_id.__eq__(class_room_id)).all()
def count_student_class(class_room_id):
    return Student.query.filter(Student.class_room_id.__eq__(class_room_id)).count()
def read_classroom_quantity(kw_grade=None, kw_class=None, page=1):
    classroom = db.session.query(ClassRoom.id, ClassRoom.name, ClassRoom.grade_id, func.count(Student.class_room_id))\
                      .join(Student, ClassRoom.id.__eq__(Student.class_room_id), isouter=True)\
                     .group_by(ClassRoom.id, ClassRoom.name, ClassRoom.grade_id)
    if kw_grade:
        classroom = classroom.filter(Grade.name.contains(kw_grade))
    if kw_class:
        classroom = classroom.filter(ClassRoom.name.contains(kw_class))

    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    end = start + page_size

    return classroom.slice(start, end).all()

def count_class():
    return ClassRoom.query.count()

def add_class(class_room_id, name): #kwargs: những thông tin không bắt buộc
    classroom = ClassRoom(class_room_id=class_room_id.strip(), name=name.strip() )
    db.session.add(classroom)
    db.session.commit()
def add_student_class(full_name, gender, birthday, phone, class_room_id,**kwargs): #kwargs: những thông tin không bắt buộc
    student_class = Student(full_name=full_name, gender=gender, birthday=birthday, phone=phone,
                              email=kwargs.get('email'), class_room_id=class_room_id)
    db.session.add(student_class)
    db.session.commit()

def count_student_class(class_room_id):
    return Student.query.filter(Student.class_room_id.__eq__(class_room_id)).count()

def count_quantity(class_room_id):
    x = count_student_class(class_room_id)
    ClassRoom.max_quantity = x
    p = 40
    if int(x) < p.max_quantity:
        return True
    else:
        return False

def list_subject():
    return Subject.query.all()

# def list_subject(kw_grade=None, kw_sj=None):
#     a = db.session.query(subject_grade.subject_id, subject.name, subject_grade.grade_name)\
#                      .join(subject, subject_grade.subject_id.__eq__(subject_id))
#     if kw_grade:
#         a = a.filter(monhoc_khoilop.grade_name.contains(kw_grade))
#     if kw_sj:
#         a = a.filter(Subject.name.contains(kw_sj))
#     return a.all()

def add_subject(subject_name): #kwargs: những thông tin không bắt buộc
    add_subject = Subject(name=subject_name)
    db.session.add(add_subject)
    db.session.commit()

def get_user_by_id(user_id):
    return User.query.get(user_id)


def load_student():
    return Student.query.all()
