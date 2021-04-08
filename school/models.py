from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=255, default='')
    student_age= models.IntegerField(default=5)
    student_gpa= models.DecimalField(decimal_places=2, max_digits=3, default=0.0) 

    def __str__(self):
        return f'{self.student_name}'

class Courses(models.Model):
    course_name = models.CharField(max_length=255, default='')
    course_description = models.CharField(max_length=1024, default='')
    students = models.ManyToManyField(Students, related_name="courses")

    def __str__(self):
        return f'{self.course_name} : {self.course_description}'