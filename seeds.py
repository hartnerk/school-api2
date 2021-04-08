from school.models import Students, Courses


s1 = Students(student_name="Greg Machat", student_age=18, student_gpa=1.5)
s1.save()
s2 = Students(student_name="Kyle Hartner", student_age=16, student_gpa=3.5)
s2.save()
s3 = Students(student_name="Doug Funny", student_age=14, student_gpa=3.3)
s3.save()


c1 = Courses(course_name="Physics", course_description="Learn the newton stuff to get that dank knowledge")
c1.save()
c1.students.add(s1)
c1.students.add(s2)

c2 = Courses(course_name="Algebra", course_description="Letters and numbers and stuff")
c2.save()
c2.students.add(s2)
c2.students.add(s3)

c3 = Courses(course_name="History", course_description="Learn about them oldies")
c3.save()
c3.students.add(s1)
c3.students.add(s2)
c3.students.add(s3)
