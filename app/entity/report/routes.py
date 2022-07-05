from flask import render_template, url_for,flash,redirect,request,abort,Blueprint







report =Blueprint('report',__name__)



@report.route('/insertreport')
def reportcard():
    form=reportForm()
    if form.validate_on_submit():
        term=form.term.data#run queries
        student=form.student.data
        subject=form.subject.data
        mark=form.mark.data
        grade=form.grade.data
        year=form.year.data
        classz=form.classz.data
        report_card=form#get you some report data
        buses=reportdata(reportcard=reportcard.id,subject_id=subject.id,mark=mark,grade=grade)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    return render_template('fabien-ui/location.html',legend="login",form=form)


