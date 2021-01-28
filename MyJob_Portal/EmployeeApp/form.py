from django import forms
from .models import *

class EmployeeForm(forms.Form):
    eid = forms.IntegerField()
    ename = forms.CharField()
    eaddr = forms.CharField()
    esalary =forms.FloatField()

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'