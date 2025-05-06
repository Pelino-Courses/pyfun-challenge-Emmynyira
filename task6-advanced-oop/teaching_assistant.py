from student import Student
from instructor import Instructor
 
class TeachingAssistant(Student,Instructor):
     """
     Class representing a teaching assistant.
     Inherits from the Instructor class.
     Attributes:
         name (str): The name of the teaching assistant.
         age (int): The age of the teaching assistant.
         courses (List[Course]): List of courses taught by the teaching assistant.
     """
     def __init__(self, name: str, age: int):
         super().__init__(name, age)
     
     def role(self) -> str:
         """
         Show the role of the teaching assistant.
         Returns:
             str: The role of the teaching assistant.
         """
         return "Teaching Assistant"
     def __str__(self):
         return f"{self.name} (Teaching assistant)"
     