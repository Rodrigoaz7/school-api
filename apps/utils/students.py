from student.models import Student
from datetime import datetime as dt

def generateRegistration():
    year = dt.now().year
    numberOfStudent = Student.objects.all().count() + 1
    return str(year) + str(numberOfStudent)