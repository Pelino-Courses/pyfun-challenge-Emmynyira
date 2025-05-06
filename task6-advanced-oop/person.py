from abc import ABC, abstractmethod
 
class Person(ABC):
     """
     Abstract base class for all persons.
     Attributes:
         name (str): The name of the person.
         age (int): The age of the person.
     """
     def __init__(self, name: str, age: int):
         if not isinstance(name, str) or not name:
             raise ValueError("Name con not be empty string.")
         self.name = name
         self.age = age
         @abstractmethod 
         def role(self) -> str:
             """
             Abstract method to show the role of a person.
             Returns:
                 str: The role of the person.
             """
             pass
         def __str__(self) -> str:
             return f"{self.rolle()}: {self.name} ({self.age} years old)"