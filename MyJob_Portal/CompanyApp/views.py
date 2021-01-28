from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import CompanyModel,JobModel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

class CompanyListView(ListView):
    model = CompanyModel
    template_name = 'CompanyApp/list.html'
    context_object_name = 'comp'

class CompanyDetailView(DetailView):
    model = CompanyModel

class CreateCompanyView(CreateView):
    model = CompanyModel
    fields = '__all__'
    # success_url = '/ca/list/'
    success_url = reverse_lazy('list')

class UpdateComapnyView(UpdateView):
    model = CompanyModel
    fields = '__all__'
    # success_url = '/ca/list/'
    success_url = reverse_lazy('list')

class DeleteComapnyView(DeleteView):
    model = CompanyModel
    # success_url = '/ca/list/'
    success_url = reverse_lazy('list')

  ### JOb Views details

class JobListView(ListView):
    model = JobModel
    template_name = 'CompanyApp/joblist.html'
    context_object_name = 'job'

class JobDetailView(DetailView):
    model = JobModel

class CreateJobView(CreateView):
    model = JobModel
    fields = '__all__'
    success_url = reverse_lazy('joblist')

class UpdateJobView(UpdateView):
    model = JobModel
    fields = '__all__'
    success_url = reverse_lazy('joblist')

class DeleteJobView(DeleteView):
    model = JobModel
    success_url = reverse_lazy('joblist')

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
                return redirect('/emp/all/')
        else:
            messages.error(request,'Invalid Credential..!!')
            return HttpResponse(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')





