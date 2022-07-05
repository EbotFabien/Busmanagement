from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from app.Models import subject,Classes,Student,Term,classyear,Year,reportcard,reportdata
from app.entity.extra.forms import CreateForm,SubjectForm,ClassForm,YearForm,StudentForm,reportForm
from app import bcrypt,db
from sqlalchemy import or_, and_, distinct, func
from app.entity.ml.utils import machine_learning






extra =Blueprint('extra',__name__)

@extra.route('/viewsubject')
def viewsubject():
    des=subject.query.all()
    return render_template('fabien-ui/viewsub.html',legend="login",des=des)

@extra.route('/insertsubject',methods=['GET','POST'])
def subjects():
    form=SubjectForm()
    if form.validate_on_submit():
        buses=subject(name=form.name.data,coefficient=form.coefficient.data,Type=form.science.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('extra.viewsubject'))
    return render_template('fabien-ui/add_sub.html',legend="login",form=form)

@extra.route('/studentyears/<id>')
def studentyears(id):
    des=classyear.query.filter_by(student_id=id).all()
    return render_template('fabien-ui/stud_yr.html',legend="login",des=des,id=id)

@extra.route('/studentterms/<id>/<stud>')
def studentterms(id,stud):
    des=reportcard.query.filter(and_(reportcard.year_id==id,reportcard.student_id==stud)).all()
    return render_template('fabien-ui/stuterms.html',legend="login",des=des,id=id,stud=stud)

@extra.route('/repodata/<id>')
def repodata(id):
    des=reportdata.query.filter_by(reportcard=id).all()
    return render_template('fabien-ui/repoda.html',legend="login",des=des,id=id)

@extra.route('/classyear/<id>')#all class for that year
def viewclassyear(id):
    des=classyear.query.filter_by(year_id=id).all()
    return render_template('fabien-ui/classenro.html',legend="login",des=des)


@extra.route('/insertclassyear',methods=['GET','POST'])
def insertclassyear():
    form=ClassForm()
    terms=Term.query.all()
    if form.validate_on_submit():
        buses=classyear(class_id=form.class_id.data,year_id=form.year_id.data,student_id=form.student_id.data)
        db.session.add(buses)
        db.session.commit()
        for i in terms:
            student_card=reportcard(Term=i.id,student_id=buses.student_id,year_id=buses.year_id)
            db.session.add(student_card)
            db.session.commit()
        return redirect(url_for('extra.viewclassyear',id=buses.year_id))
    return render_template('fabien-ui/add_c_s.html',legend="login",form=form)



@extra.route('/viewclass')
def viewclass():
    des=Classes.query.all()
    return render_template('fabien-ui/viewclass.html',legend="login",des=des)

@extra.route('/insertclass',methods=['GET','POST'])
def classes():
    form=CreateForm()
    if form.validate_on_submit():
        buses=Classes(name=form.name.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('extra.viewclass'))
    return render_template('fabien-ui/add_class.html',legend="login",form=form)

@extra.route('/viewstudents')
def viewstudents():
    des=Student.query.all()
    return render_template('fabien-ui/view_stud.html',legend="login",des=des)

@extra.route('/insertstudents',methods=['GET','POST'])
def students():
    form=StudentForm()
    if form.validate_on_submit():
        time=form.enrollement.data#put date here
        buses=Student(name=form.name.data,enrollement=time)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('extra.viewstudents'))
    return render_template('fabien-ui/add_student.html',legend="login",form=form)

@extra.route('/viewterms')
def viewterms():
    des=Term.query.all()
    return render_template('fabien-ui/viewterm.html',legend="login",des=des)

@extra.route('/insertterms',methods=['GET','POST'])
def terms():
    form=CreateForm()
    if form.validate_on_submit():
        buses=Term(name=form.name.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('extra.viewterms'))
    return render_template('fabien-ui/add_term.html',legend="login",form=form)


@extra.route('/viewyears')
def viewyears():
    des=Year.query.all()
    return render_template('fabien-ui/allyears.html',legend="login",yrs=des)

@extra.route('/insertyears',methods=['GET','POST'])
def years():
    form=YearForm()
    if form.validate_on_submit():
        buses=Year(name=form.Year.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    return render_template('fabien-ui/add_year.html',legend="login",form=form)


@extra.route('/reportdat/<id>',methods=['GET','POST'])
def reportdat(id):
    form=reportForm()
    if form.validate_on_submit():
        buses=reportdata(reportcard=id,subject_id=form.subject.data,mark=form.mark.data)
        db.session.add(buses)
        db.session.commit()
        if buses.mark >= 15 and buses.mark < 18: 
            buses.grade='B'
        if buses.mark >= 18 : 
            buses.grade='A'
        if buses.mark < 15 : 
            buses.grade='C'
        if buses.mark < 10 : 
            buses.grade='D'
        db.session.commit()
        
        return redirect(url_for('extra.repodata',id=id))
    return render_template('fabien-ui/add_report.html',legend="login",form=form)


@extra.route('/machinelearning/<id>/<stud>')#all class for that year
def machine(id,stud):
    des=reportcard.query.filter(and_(reportcard.year_id==id,reportcard.student_id==stud)).all()
    rep=machine_learning(des) 
    return render_template('fabien-ui/ml.html',rep=rep)

