from django.urls import path, include
from . import views

app_name = 'school'

urlpatterns = [
    path("students/", views.all_students, name="all_students"),
    path("students/new/", views.new_student, name="new_student"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
    path("students/<int:student_id>/edit/", views.edit_student, name="edit_student"),
    path("students/<int:student_id>/delete/", views.delete_student, name="delete_student"),
    
    path("courses/", views.all_courses, name="all_courses"),
    path("courses/new/", views.new_course, name="new_courses"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path("courses/<int:course_id>/edit/", views.edit_course, name="edit_course"),
    path("courses/<int:course_id>/delete/", views.delete_course, name="delete_course"),
    path("courses/<int:course_id>/enroll/<int:student_id>/", views.enroll_student, name="enroll_student"),
    path("courses/<int:course_id>/remove/<int:student_id>/", views.remove_student, name="remove_student"),
    path("students/<int:student_id>/classes/", views.student_classes, name="student_classes"),
    path("courses/<int:course_id>/students/", views.classes_students, name="classes_students"),
]