from app import db, app
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, backref


class Person(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=False)
    birthday = Column(Date)
    phone = Column(String(50))
    email = Column(String(255))


teach_detail = db.Table('teach_detail', Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('startDate', Date, nullable=True),
                        Column('teacher_id', Integer, ForeignKey('teacher.id'), nullable=True),
                        Column('subject_id', Integer, ForeignKey('subject.id'), nullable=True))


class Teacher(Person):
    __tablename__ = 'teacher'
    identity = Column(String(100), nullable=False)
    degree = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))
    teach_details = relationship('Subject', secondary='teach_detail', lazy=True, backref=backref('teacher', lazy=True))

    def __str__(self):
        return self.full_name


class Grade(db.Model):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    class_room = relationship('ClassRoom', backref='grade', lazy=True)

    def __str__(self):
        return self.name


class ClassRoom(db.Model):
    __tablename__ = 'class_room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    max_quantity = Column(Integer, nullable=False)
    students = relationship('Student', backref='class_room', lazy=True)
    grade_id = Column(Integer, ForeignKey(Grade.id, ondelete='restrict', onupdate='restrict'), nullable=False)

    def __str__(self):
        return self.name


class Student(Person):
    __tablename__ = 'student'
    class_room_id = Column(Integer, ForeignKey(ClassRoom.id, ondelete='restrict', onupdate='restrict'), nullable=False)

    def __str__(self):
        return self.full_name


class ScoreType(db.Model):
    __tablename__ = 'score_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    scores = relationship('Score', backref='score_type', lazy=True)

    def __str__(self):
        return self.name


class Semester(db.Model):
    __tablename__ = 'semester'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    note = Column(String(255))
    scores = relationship('Score', backref='semester', lazy=True)

    def __str__(self):
        return self.name


class Subject(db.Model):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __str__(self):
        return self.name


class Score(db.Model):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Float, default=0)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete='cascade', onupdate='cascade'), nullable=True)
    score_type = Column(Integer, ForeignKey(ScoreType.id, ondelete='cascade', onupdate='cascade'), nullable=True)
    semester_id = Column(Integer, ForeignKey(Semester.id, ondelete='cascade', onupdate='cascade'), nullable=True)
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete='cascade', onupdate='cascade'), nullable=True)

    def __str__(self):
        return self.score


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
