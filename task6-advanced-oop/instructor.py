from person import Person
from typing import Iterator, List

class Instructor(Person):
    """
    Class representing an instructor.
    Inherits from the Person class.
    Attributes:
        name (str): The name of the instructor.
        age (int): The age of the instructor.
        courses (List[Course]): List of courses taught by the instructor.
    """
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.courses : List ['Course'] = []
    def get_courses(self) -> Iterator['Course']:
        return iter(self.courses)

    def add_course(self, course: 'Course'):
        """
        Add a course to the instructor's list of courses.
        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)
        course.instructor = self
    def role(self) -> str:
        """
        Show the role of the instructor.
        Returns:
            str: The role of the instructor.
        """
        return "Instructor"
    def courses(self) -> Iterator['Course']:
        """
        Get an iterator over the courses taught by the instructor.
        Returns:
            Iterator[Course]: An iterator over the courses.
        """
        return iter(self.courses)
        


    