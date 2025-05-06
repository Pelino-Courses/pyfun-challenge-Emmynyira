from student import Student
from instructor import Instructor
from course import Course
from teaching_assistant import TeachingAssistant
 
 # create peaple
stud1= Student("Eric", 20)
instruct= Instructor("Dr. Smith", 45)
teach= TeachingAssistant("Emmy", 30)
 
 # create course
math= Course("Math 101",credits=3)
lab= Course.create_lab_course("Physics Lab")
 # assign instructor
instruct.add_course(math)
 # Enroll students
stud1.enroll(math)
stud1.enroll(lab)
teach.enroll(math)
 # Ta teaches the course
teach.add_course(lab)
 # print the courses
print("Courses Eric is enrolled in:")
for course in stud1.get_courses():
     print("-", course)
print("\n Students in Math 101:")
for student in math.students():
     print("-", student)
print("\n courses taught by Dr. Smith:")
for course in instruct.get_courses():
     print("-", course)
 # operations
combined_courses= stud1 + teach
print(f"\n Combined courses of Eric and Emmy:{[c.title for c in combined_courses]}")
 # course credits sum
total_credits= math + lab
print(f"\n Total credits of Math 101 and Physics Lab: {total_credits}")