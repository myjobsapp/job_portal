from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required(login_url='/ea/login/')
def emp_register(request):
    if request.method == 'POST':
        emp1 = EmployeeForm(request.POST)
        if emp1.is_valid():
            id = emp1.cleaned_data['eid']
            name = emp1.cleaned_data['ename']
            addr = emp1.cleaned_data['eaddr']
            salary = emp1.cleaned_data['esalary']
            emp = EmployeeModel(eid=id,ename=name,eaddr=addr,esalary=salary)
            emp.save()
            return redirect('all_emp')
    elif request.method == 'GET':
        emp = EmployeeForm()
        return render(request,'register.html',{'emp':emp})

#@login_required(login_url='/ea/login/')
def all_emp(request):
    emp = EmployeeModel.objects.all()
    return render(request,'all.html',{'emp':emp})

def emp_update(request,oid):
    emp = EmployeeModel.objects.get(pk=oid)
    if request.method == 'GET':
        emp1 = EmployeeUpdateForm(instance=emp)
    elif request.method == 'POST':
        emp1 = EmployeeUpdateForm(request.POST,instance=emp)
        if emp1.is_valid():
            emp1.save()
            return redirect('all_emp')
    return render(request,'update.html',{'emp1':emp1})

def emp_delete(request,oid):
    empd = EmployeeModel.objects.get(pk=oid)
    if request.method == 'GET':
        print('Get req revd...')
        context = {'empd': empd}
        template_name = 'delete.html'
        return render(request, template_name, context)

    elif request.method == 'POST':
        print('Post req recvd...')
        empd = EmployeeModel.objects.get(pk=oid)
        empd.delete()
        return redirect('all_emp')

def usercreation(request):
    if request.method == 'GET':
        u = UserCreationForm()
    if request.method == 'POST':
        u = UserCreationForm(request.POST)
        if u.is_valid():
            u.save()
            return redirect('login')
    template_name = 'usercreation.html'
    context = {'u':u}
    return render(request,template_name,context)

def userlogin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        uname = request.POST['uname']
        pw = request.POST['pw']
        user = authenticate(username=uname,password=pw)

        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/ca/joblist/')
        else:
            messages.error(request,'Invalid Credential..!!')
            return HttpResponse(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')






