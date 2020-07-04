from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):

    name = models.CharField('Name', max_length=100, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False)
    date_birth = models.DateField('Date of birth', null=False, blank=False, auto_now_add=False)
    registration = models.CharField('Registration of the student in school', 
        null=False, blank=False, max_length=12,
        help_text='Number of registration. The first numbers are the current year')

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name + " (" + self.registration + ")"