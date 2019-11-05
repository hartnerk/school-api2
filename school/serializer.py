from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Student
    fields = ['name', 'grade']

class CourseSerializer(serializers.ModelSerializer):
  students = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Student.objects.all())
  # students = StudentSerializer(many=True, read_only=False)

  class Meta:
    model = Course
    fields = ['name', 'description', 'students']

  # def create(self, validated_data):
  #   students_data = validated_data.pop('students')
  #   course = Course.objects.create(**validated_data)
  #   # for student in students_data:
  #   #   Student.objects.create(courses=course, **student)
  #   return course

  # def update(self, instance, validated_data):
  #   pass
