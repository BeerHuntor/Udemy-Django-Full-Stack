import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from ProTwo_app.models import Users

fake = Faker()

def deleteData():
    Users.objects.all().delete()

def addUser():
    name = fake.name().split()
    first_name = name[0]
    last_name = name[-1]
    email = fake.email()
    user = Users.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
    user.save()
    return user

def populate(N=5):
    for entry in range(N):
        addUser()

if __name__ == '__main__':
    print('Populating Entries!')
    deleteData()
    populate(20)