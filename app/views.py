from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_Dept_Form(request):
    
    if request.method == 'POST':
        dno = request.POST['dno']
        dn = request.POST['dn']
        lo = request.POST['lo']
        DO = Dept.objects.get_or_create(dept_no=dno,dept_name=dn,loc=lo)[0]
        DO.save()
        return HttpResponse('<center><h1>Department Created</h1></center>')
    return render(request,'insert_Dept_Form.html')


def insert_Emp_Form(request):
    
    DO = Dept.objects.all()
    d = {'DO':DO}
    if request.method == 'POST':
        dno = request.POST['dno']
        eid = request.POST['eid']
        en = request.POST['en']
        jb = request.POST['jb']
        sl = request.POST['sl']
        hd = request.POST['hd']
        
        DO = Dept.objects.get(dept_no=dno)
        DO.save()
        print(DO,type(DO))
        EO = Emp.objects.get_or_create(emp_id=eid,emp_name=en,job=jb,sal=sl,hire_date=hd,dept_no=DO)[0]
        EO.save()
        return HttpResponse('<center><h1>Employee Created</h1></center>') 
    return render(request,'insert_Emp_Form.html',d)


def retrieve_Dept(request):
    DO = Dept.objects.all()
    d = {'DO':DO}
    if request.method == 'POST':
        LD = request.POST.getlist('dn')
        RD = Dept.objects.none()
        print(LD)
        for i in LD:
            RD = RD|Dept.objects.filter(dept_no=i)
        
        print(RD)
        d1 = {'RD':RD}
        return render(request,'dept_Data.html',d1)
    return render(request,'retrieve_Dept.html',d)


def retrieve_Emp(request):
    EO = Emp.objects.all()
    d = {'EO':EO}
    if request.method == 'POST':
        LE = request.POST.getlist('en')
        RE = Emp.objects.none()
        
        for i in LE:
            RE = RE|Emp.objects.filter(emp_name=i)
        d1 = {'RE':RE}
        return render(request,'emp_Data.html',d1)
    return render(request,'retrieve_Emp.html',d)

def dept_checkbox(request):
    DO = Dept.objects.all()
    d = {'DO':DO}
    return render(request,'dept_Checkbox.html',d)

def emp_checkbox(request):
    EO = Emp.objects.all()
    d = {'EO':EO}
    return render(request,'emp_checkbox.html',d)