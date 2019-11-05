from .models import Student, Course
from .serializer import StudentSerializer, CourseSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  @action(detail=True)
  def courses(self, request, pk=None):
    student = self.get_object()
    courses = Course.objects.filter(students=student)
    context = {
      'request': request
    }
    course_serializer = CourseSerializer(courses, many=True, context=context)
    return Response(course_serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  @action(detail=True)
  def students(self, request, pk=None):
    course = self.get_object()
    students = Student.objects.filter(courses=course)
    context = {
      'request': request
    }
    student_serializer = StudentSerializer(students, many=True, context=context)
    return Response(student_serializer.data)
