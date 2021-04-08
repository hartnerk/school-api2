from django.shortcuts import render
from django.http import JsonResponse
from .models import Students, Courses
from .serializers import StudentSerializer, CourseSerializer
from .forms import StudentForm, CourseForm
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def all_students(request):
    students = Students.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)
    

def student_detail(request, student_id):
    student = Students.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).student_detail
    return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def new_student(request):
    if request.method=='POST':
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student_form = form.save(commit=False)
            form.save()
            serialized_student = StudentSerializer(student_form).student_detail
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def edit_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method =='POST':
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student_form = form.save(commit=False)
            form.save()
            serialized_student = StudentSerializer(student_form).student_detail
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return JsonResponse(data={'status': 'Successfully deleted student from record'}, status=200)

# ------- COURSES -------
def all_courses(request):
    courses = Courses.objects.all()
    serialized_courses = CourseSerializer(courses).all_courses
    return JsonResponse(data=serialized_courses, status=200)
    

def course_detail(request, course_id):
    course = Courses.objects.get(id=course_id)
    serialized_course = CourseSerializer(course).course_detail
    return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def new_course(request):
    if request.method=='POST':
        data = json.load(request)
        form = CourseForm(data)
        if form.is_valid():
            course_form = form.save(commit=False)
            form.save()
            serialized_course = CourseSerializer(course_form).course_detail
            return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    if request.method =='POST':
        data = json.load(request)
        form = CourseForm(data, instance=course)
        if form.is_valid():
            course_form = form.save(commit=False)
            form.save()
            serialized_course = CourseSerializer(course_form).course_detail
            return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        return JsonResponse(data={'status': 'Successfully deleted course from record'}, status=200)

@csrf_exempt
def enroll_student(request, course_id, student_id):
    course = Courses.objects.get(id=course_id)
    student = Students.objects.get(id=student_id)
    if request.method == "POST":
        course.students.add(student)
        serialized_course = CourseSerializer(course).course_detail
        return JsonResponse(data=serialized_course, status=200)


@csrf_exempt
def remove_student(request, course_id, student_id):
    course = Courses.objects.get(id=course_id)
    student = course.students.get(id=student_id)
    if request.method == "POST":
        course.students.remove(student)
        serialized_course = CourseSerializer(course).course_detail
        return JsonResponse(data=serialized_course, status=200)

def student_classes(request, student_id):
    student = Students.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).student_detail
    return JsonResponse(data=serialized_student['courses'], status=200)

def classes_students(request, course_id):
    course = Courses.objects.get(id=course_id)
    serialized_course= CourseSerializer(course).course_detail
    return JsonResponse(data=serialized_course['students'], status=200)
