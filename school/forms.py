from school.models import Students, Courses
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['student_name', 'student_age', 'student_gpa']

class CourseForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name', 'course_description']
        