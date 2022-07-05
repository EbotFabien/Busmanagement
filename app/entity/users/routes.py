from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from app.entity.users.forms import LoginForm,RegistrationForm
from app.Models import User,Term,Student,Classes,reportcard,Year,subject
from app import bcrypt,db
from datetime import date,timedelta,datetime,timezone 





users =Blueprint('users',__name__)

@users.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        if current_user.Type=='Admin':
            return redirect(url_for('users.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        name=User.query.filter_by(username=form.username.data).first()#put login
        if  name and bcrypt.check_password_hash(name.password,form.password.data):
            login_user(name,remember=form.remember.data,duration=timedelta(seconds=30)) 
            next_page=request.args.get('next') 
            return redirect (next_page) if next_page else  redirect(url_for('users.dashboard'))
        else:
    
            flash(f'Mauvais Identifiant ou mot de passe, essayez à nouveau','danger')

    return render_template('fabien-ui/login.html',legend="login",form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))



@users.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if current_user.is_authenticated:
       return redirect(url_for('users.dashboard'))
    form = RegistrationForm()

    if form.validate_on_submit():#check user 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,Type=form.type.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created you can now login','success')
        return redirect(url_for('users.login'))
    return render_template('fabien-ui/register.html',legend="sign_up",form=form)


@users.route('/dashboard',methods=['GET','POST'])
def dashboard():
    terms=subject.query.count()
    students=Student.query.count()
    classes=Classes.query.count()
    report=reportcard.query.count()
    year=Year.query.count()
    return render_template('fabien-ui/index.html',classes=classes,term=terms,students=students,reportcard=report,year=year)