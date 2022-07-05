from flask import current_app
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKeyConstraint,ForeignKey,UniqueConstraint

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
   # image_file =db.Column(db.String(20),nullable=False,default='Billgates.jpg')
    password = db.Column(db.String(60),nullable=False)
    Type= db.Column(db.String(60),nullable=False)


    def get_reset_token(self,expire_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expire_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
        
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token) ['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Classes(db.Model):
    __tablename__ = 'Classes'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __repr__(self):
        return '<Classes %r>' %self.id


class Term(db.Model):
    __tablename__ = 'Term'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __repr__(self):
        return '<Term %r>' %self.id

class Year(db.Model):
    __tablename__ = 'Year'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __repr__(self):
        return '<Year %r>' %self.id

class subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    coefficient=db.Column(db.Integer)
    Type=db.Column(db.String)

    def __repr__(self):
        return '<subject %r>' %self.id


class Student(db.Model):
    __tablename__ = 'Student'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    enrollement=db.Column(db.Integer, ForeignKey('Year.id'))
    enrol__=db.relationship("Year", 
            primaryjoin=(enrollement == Year.id),
            backref=db.backref('enrol__nego',  uselist=False),  uselist=False)
    status =db.Column(db.Boolean,default=True)

    def __repr__(self):
        return '<Student %r>' %self.id

class classyear(db.Model):
    __tablename__ = 'classyear'

    id = db.Column(db.Integer,primary_key=True)
    class_id=db.Column(db.Integer, ForeignKey('Classes.id'))
    student_id=db.Column(db.Integer, ForeignKey('Student.id'))
    year_id=db.Column(db.Integer, ForeignKey('Year.id'))
    year__=db.relationship("Year", 
            primaryjoin=(year_id == Year.id),
            backref=db.backref('year__nego',  uselist=False),  uselist=False)


    def __repr__(self):
        return '<classyear %r>' %self.id


class reportcard(db.Model):
    __tablename__ = 'reportcard'

    id = db.Column(db.Integer,primary_key=True)
    Term=db.Column(db.Integer, ForeignKey('Term.id'))
    student_id=db.Column(db.Integer, ForeignKey('Student.id'))
    year_id=db.Column(db.Integer, ForeignKey('Year.id'))
    average=db.Column(db.Integer)


    def __repr__(self):
        return '<reportcard %r>' %self.id


class reportdata(db.Model):
    __tablename__ = 'reportdata'

    id = db.Column(db.Integer,primary_key=True)
    reportcard=db.Column(db.Integer, ForeignKey('reportcard.id'))
    subject_id=db.Column(db.Integer, ForeignKey('subject.id'))
    subject__=db.relationship("subject", 
            primaryjoin=(subject_id == subject.id),
            backref=db.backref('client__nego',  uselist=False),  uselist=False)
    mark=db.Column(db.Integer)
    grade=db.Column(db.String)


    def __repr__(self):
        return '<reportdata %r>' %self.id