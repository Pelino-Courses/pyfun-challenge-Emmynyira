class Enrollment:
     def __init__(self, student: 'Student', course: 'Course'):
         """
         Initialize an enrollment for a student in a course.
         Args:
             student (Student): The student enrolling in the course.
             course (Course): The course the student is enrolling in.
         """
         self.student = student
         self.course = course
     def __str__(self) :
         """
         Returns a string representation of the enrollment.
         Returns:
             str: human readable string representation.
         """
         return f"{self.student.name} enrolled in {self.course.title}"