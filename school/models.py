from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=100)
  grade = models.CharField(max_length=100)

  def __str__(self):
    return f'id: {self.id} name: {self.name}'

class Course(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  students = models.ManyToManyField(Student, related_name='courses')

  def __str__(self):
    return f'id: {self.id} name: {self.name}'
