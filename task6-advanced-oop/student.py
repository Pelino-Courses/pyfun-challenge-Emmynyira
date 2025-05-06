from person import Person
from typing import List,Iterator
import uuid
from enrollment import Enrollment
 
class Student(Person):
     """
     Class representing a student.
     Inherits from the Person class.
     Attributes:
         name (str): The name of the student.
         age (int): The age of the student.
         student_id (str): The unique ID of the student.
         enrollments (List[Enrollment]): List of enrollments for the student.
     """
     def __init__(self, name: str, age: int,student_id: str = None):
         super().__init__(name, age)
         self.student_id = student_id or str(uuid.uuid4())
         self._enrollments: List['Enrollment'] = []
     def get_courses(self) -> Iterator['Course']:
          return (enrollment.course for enrollment in self._enrollments)
 
     def enroll(self, course: 'Course'):
         """
         Enroll the student in a course.
         Args:
             course (Course): The course to enroll in.
         """
         enrollment = Enrollment(self, course)
         self._enrollments.append(enrollment)
         course.enrollments.append(enrollment)
     def courses(self) -> Iterator['Course']:
         """
         Get an iterator over the courses the student is enrolled in.
         Returns:
             Iterator[Course]: An iterator over the courses.
         """
         return (enrollment.course for enrollment in self._enrollments)
             
     def __add__(self, other: 'Student') -> List['Course']:
         """
         Combine the courses of two students.
         Args:
             other (Student): The other student.
         Returns:
             List[Course]: List of combined courses.
         """
         return list(set(self.courses())| set(other.get_courses()))
     def role(self) -> str:
         """
         Show the role of the student.
         Returns:
             str: The role of the student.
         """
         return "Student"
     def __str__(self):
         """
         Returns a string representation of the student.
         Returns:
             str: The string representation.
         """
         return f"Student(name={self.name} , Age= {self.age},student ID ={self.student_id})"