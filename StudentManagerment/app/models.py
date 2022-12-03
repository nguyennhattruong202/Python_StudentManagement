from enum import Enum as UserEnum
from app import db, app
from sqlalchemy import Column, Integer, String, Date, Enum, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
import hashlib


class UserRole(UserEnum):
    ADMIN = 1
    TEACHER = 2
    EMPLOYEE = 3


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Person(BaseModel):
    __abstract__ = True
    full_name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=False)
    birthday = Column(Date, nullable=True)
    phone = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)


class User(Person):
    __tablename__ = 'user'
    identity = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    user_role = Column(Enum(UserRole), nullable=False)
    teach_detail = relationship('TeachDetail', backref='user', lazy=True)

    def __str__(self):
        return self.full_name


class Student(Person):
    __tablename__ = 'student'
    class_room_id = Column(Integer, ForeignKey('class_room.id', ondelete='restrict', onupdate='restrict'),
                           nullable=True)
    scores = relationship('Score', backref='student', lazy=True)

    def __str__(self):
        return self.full_name


class ClassRoom(BaseModel):
    __tablename__ = 'class_room'
    name = Column(String(255), nullable=False)
    max_quantity = Column(Integer, nullable=False)
    grade_id = Column(Integer, ForeignKey('grade.id', ondelete='restrict', onupdate='restrict'), nullable=False)
    students = relationship('Student', backref='class_room', lazy=True)

    def __str__(self):
        return self.name


class Grade(BaseModel):
    __tablename__ = 'grade'
    name = Column(String(255), nullable=False)
    class_rooms = relationship('ClassRoom', backref='grade', lazy=True)

    def __str__(self):
        return self.name


class Score(BaseModel):
    __tablename__ = 'score'
    score = Column(Float, default=0)
    student_id = Column(Integer, ForeignKey(Student.id, onupdate='cascade', ondelete='cascade'), nullable=False)
    score_type_id = Column(Integer, ForeignKey('score_type.id', ondelete='cascade', onupdate='cascade'), nullable=False)
    semester_id = Column(Integer, ForeignKey('semester.id', ondelete='cascade', onupdate='cascade'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id', ondelete='cascade', onupdate='cascade'), nullable=False)


class Semester(BaseModel):
    __tablename__ = 'semester'
    name = Column(String(255), nullable=False)
    note = Column(Text, nullable=True)
    scores = relationship('Score', backref='semester', lazy=True)

    def __str__(self):
        return self.name


class ScoreType(BaseModel):
    __tablename__ = 'score_type'
    name = Column(String(255), nullable=False)
    scores = relationship('Score', backref='score_type', lazy=True)

    def __str__(self):
        return self.name


class Subject(BaseModel):
    __tablename__ = 'subject'
    name = Column(String(255), nullable=False)
    scores = relationship('Score', backref='subject', lazy=True)
    teach_details = relationship('TeachDetail', backref='subject', lazy=True)

    def __str__(self):
        return self.name


class TeachDetail(BaseModel):
    __tablename__ = 'teach_detail'
    startDate = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete='restrict', onupdate='restrict'), nullable=True)
    subject_id = Column(Integer, ForeignKey(Subject.id, onupdate='restrict', ondelete='restrict'), nullable=True)


# if __name__ == '__main__':
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
#         password_user = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
#         user1 = User(full_name='Hoàng Công Minh', gender='Nam', birthday='2001-07-25', phone='0909291469',
#                      email='1951012069minh@ou.edu.vn', identity='097201000060', degree='Thạc sĩ', position='Giáo viên',
#                      username='congminh', password=password_user, user_role=UserRole.TEACHER)
#         user2 = User(full_name='Nguyễn Duy Hải Anh', gender='Nam', birthday='2001-04-05', phone='0941996309',
#                      email='1951052009anh@ou.edu.vn', identity='097201006660', position='Admin',
#                      username='haianh', password=password_user, user_role=UserRole.ADMIN)
#         user3 = User(full_name='Nguyễn Nhật Trường', gender='Nam', birthday='2001-02-20', phone='0865789234',
#                      email='1951012146truong@ou.edu.vn', identity='073301005567', position='Nhân viên',
#                      username='nhattruong', password=password_user, user_role=UserRole.EMPLOYEE)
#         db.session.add_all([user1, user2, user3])
#         db.session.commit()
#         grade1 = Grade(name='Khối 9')
#         grade2 = Grade(name='Khối 10')
#         grade3 = Grade(name='Khối 11')
#         grade4 = Grade(name='Khối 12')
#         db.session.add_all([grade1, grade2, grade3, grade4])
#         db.session.commit()
