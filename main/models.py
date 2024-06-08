from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    subject = models.CharField(max_length=255)
    

class Class(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher, blank=True)  # Allow classes without teachers


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
            