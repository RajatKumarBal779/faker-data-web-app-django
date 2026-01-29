import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import Student


def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fake = Faker()
        froll = fake.random_int(min=1,max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1,max=100)
        femail = fake.email()
        fphno = phonenumbergen()
        faddr = fake.city()
        #Loading data to table.
        Student.objects.get_or_create(
            rollno=froll,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phnumber=fphno,
            address=faddr,
        )
n=int(input('Enter No of Records :'))
populate(n)
print(f'{n} Records Inserted Successfully.....')
        