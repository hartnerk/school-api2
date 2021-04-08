from builtins import object

class StudentSerializer(object):
    def __init__(self, students):
        self.students = students

    @property
    def all_students(self):
        output = {'students': []}

        for student in self.students:
            studentInfo = {
                'student_name': student.student_name,
                'student_age': student.student_age,
                'student_gpa': student.student_gpa
            }
            output['students'].append(studentInfo)
        return output

    @property
    def student_detail(self):
        return{
            'student_name': self.students.student_name,
            'student_age': self.students.student_age,
            'student_gpa': self.students.student_gpa,
            'courses' : CourseSerializer(self.students.courses.all()).all_courses['courses']
        }


class CourseSerializer(object):
    def __init__(self, courses):
        self.courses = courses


    @property
    def all_courses(self):
        output = {'courses': []}
        for course in self.courses:
            courseInfo = {
                'course_name': course.course_name,
                'course_description': course.course_description,
            }
            output['courses'].append(courseInfo)
        return output

    @property
    def course_detail(self):
        courseInfo = {
            'course_name': self.courses.course_name,
            'course_description': self.courses.course_description,
            'students' : StudentSerializer(self.courses.students.all()).all_students['students']
        }
        return courseInfo