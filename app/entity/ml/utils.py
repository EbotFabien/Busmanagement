
from app.Models import subject,Classes,Student,Term,classyear,Year,reportcard,reportdata
from flask import current_app as app

def machine_learning(term):
    results={'S':[0,0],'A':[0,0]} #Nested dicionary structure
    peak=300
    for i in term:#nested for loops
        with app.app_context():
            k=reportdata.query.filter_by(reportcard=i.id).all()
            for sub in k:
                if  sub.subject__.Type == 'science':
                    results['S'][0]+=sub.mark
                if  sub.subject__.Type == 'arts':
                    results['A'][0]+=sub.mark

    
    for index in results:#calculate percentages
        div=results[index][0]/peak
        per=div * 100
        results[index][1]=per
    
    #Decision Tree structure
    s=[]
    a=[]
    for index in results:
    
        if index == 'S':
            if results[index][1] >= 80:
                s.append(2)# super eligible
                s.append(results[index][1])
            if results[index][1] >= 50 and results[index][1] < 80:
                s.append(1)# eligible
                s.append(results[index][1])
            if results[index][1] < 50:
                s.append(0)
                s.append(results[index][1]) # not eligible
        if index == 'A':
            if results[index][1] >= 80:
                a.append(2)# super eligible
                a.append(results[index][1])
            if results[index][1] >= 50 and  results[index][1] < 80:
                a.append(1)# eligible
                a.append(results[index][1])
            if results[index][1] <  50:
                a.append(0) # not eligible
                a.append(results[index][1])
    
   
    if s[0] == 2 and a[0] == 2:
        g="good for all with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#3
    if s[0] == 2 and a[0] <= 1:
        g="good for science only with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#2.5
    if a[0] == 2 and s[0] <= 1:
        g="good for arts only with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#2.5
    if a[0] == 1 and s[0] == 1:
        g="average for all with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#1
    if a[0] == 1 and s[0] == 0:
        g="average for arts only with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#0.5
    if s[0] == 1 and a[0] == 0:
        g="average for science only with a percentage of " +str(s[1])+" for science and " +str(a[1])+" for arts"
        return g#0.5
    
    
        
