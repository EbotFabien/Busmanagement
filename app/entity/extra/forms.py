from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,BooleanField,SelectField #, TextAreaField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from app.Models import User
from wtforms.fields.html5 import DateField




class RegistrationForm(FlaskForm):
    username =StringField('UserName',
                                validators=[DataRequired(),length(min=4 ,max=20)])
    email =StringField('Email',
                           validators=[DataRequired(),Email()])
    password =PasswordField('Password',
                                  validators=[DataRequired(),length(min=8 ,max=20)])
    confirm_password =PasswordField('ConfirmPassword',
                                  validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('This username is taken.Please choose a different name')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('This email is already used by  another user')

class CreateForm(FlaskForm):
    name =StringField('Name',
                                     validators=[DataRequired()] )                            
    submit = SubmitField('Submit')

class YearForm(FlaskForm):
    Year =StringField('Year',
                                     validators=[DataRequired()] )                           
    submit = SubmitField('Submit')

class SubjectForm(FlaskForm):
    name =StringField('Name',
                                     validators=[DataRequired()] )    
    coefficient=IntegerField('coefficient',
                                     validators=[DataRequired()] )  
    science=SelectField('Type',
                             choices=[('science','science'), ('arts','arts')])                       
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    name =StringField('Name',
                                     validators=[DataRequired()] )    
    enrollement=IntegerField('enrollement_year_id',
                                     validators=[DataRequired()] )                        
    submit = SubmitField('Submit')

class ClassForm(FlaskForm):
    class_id =IntegerField('class_id',
                                     validators=[DataRequired()] )
    year_id =IntegerField('year_id',
                                     validators=[DataRequired()] )
    student_id =IntegerField('student_id',
                                     validators=[DataRequired()] )
    submit = SubmitField('Submit')

class reportForm(FlaskForm):
    subject =IntegerField('subject_id',
                                     validators=[DataRequired()] )
    mark =IntegerField('mark_id',
                                     validators=[DataRequired()] )
    submit = SubmitField('Submit')