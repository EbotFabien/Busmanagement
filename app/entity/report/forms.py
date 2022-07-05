from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField #, TextAreaField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from app.Models import User





class reportForm(FlaskForm):
    term =StringField('UserName',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )
    year =StringField('year',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )
    student =StringField('student',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )
    mark =StringField('mark',
                                     validators=[DataRequired(),length(min=4 ,max=20)] ) 
    grade =StringField('grade',
                                     validators=[DataRequired(),length(min=4 ,max=20)] ) 
    subject =StringField('subject',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )
    classz =StringField('class',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )                       
    submit = SubmitField('Submit')