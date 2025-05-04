from typing import List, Optional, Iterator
from descriptor import PositiveInt

class Course:
    credits= PositiveInt("credits")
    """
    Class representing a course.
    Attributes:
        title (str): The title of the course.
        credits (int): The number of credits for the course.
        """
    def __init__(self, title: str, credits: int):
        self.title = title
        self.credits = credits
        self.enrollments: List['Enrollment'] = []  # List of enrollments for the course.
        self.instructor: Optional['Instructor'] = None  # Instructor for the course.
    @classmethod
    def create_lab_course(cls, title: str) -> 'Course':
        """
        Create a lab course with the given title.
        Args:
            title (str): The title of the lab course.
        Returns:
            Course: A new Course object representing the lab course.
        """
        return cls(title, credits=3)
    
    def students(self) -> Iterator['Student']:
        """
        Get an iterator over the students enrolled in the course.
        Returns:
            Iterator[Student]: An iterator over the students.
        """
        for enrollment in self.enrollments:
            yield enrollment.student
    def __str__(self) :
        """
        Returns a string representation of the course.
        Returns:
            str: human readable string representation.
        """
        return f"{self.title} ({self.credits} credits)"
    def __add__(self, other: 'Course') -> int:
        """
        Add the credits of two courses.
        Args:
            other (Course): The other course.
        Returns:
            int: Total credits of the two courses.
        """
        return self.credits + other.credits