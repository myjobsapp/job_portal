import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","MyJob_Portal.settings")

import django
django.setup()

import random
from faker import Faker
fake = Faker()

from EmployeeApp.models import EmployeeModel

def populate_customer(rows):
    for i in range(rows):
        i = random.randint(1,9)
        n = fake.name()
        a = fake.address()
        s = random.randint(10000,100000)
        obj = EmployeeModel(eid=i,ename=n,eaddr=a,esalary=s)
        obj.save()
        print('fake data added')
populate_customer(5)

'''
class Employee():

    def __init__(self,eid,ename,eaddr,esalary):
        self.eid = eid
        self.ename = ename
        self.eaddr = eaddr
        self.esalary = esalary

    def __str__(self):
        return 'employee id:{}\n name:{}\n addr:{}\n salary:{}\n'.format(self.eid,self.ename,self.eaddr,self.esalary)

#obj=0
n=5
for x in range(n):
    i = random.randint(1,9)
    n = fake.name()
    a = fake.address()
    s = random.randint(10000,100000)

    obj = Employee(eid=i,ename=n,eaddr=a,esalary=s)
    print(obj)
    '''





