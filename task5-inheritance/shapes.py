from math import pi,sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
 
 """
   Abstract base class for all geometric shapes.
   Attributes:
  color (str): The color of the shape.
  """
 def __init__(self, color: str):
        if not isinstance(color, str):
             raise ValueError("Color must be a string.")
        self.color = color

 @abstractmethod  
 def area(self) -> float:
        """
        Abstract method to calculate the area of the shape.
        Returns:
            float: The area of the shape.
        """
        pass
 @abstractmethod
 def perimeter(self) -> float:
        """
        Abstract method to calculate the perimeter of the shape.
        Returns:
            float: The perimeter of the shape.
        """
        pass
 def __str__(self) -> str:
      """
        Returns a string representation of the shape.
    Returns:
    str: human readable string representation.
    """
      return f" {self.__class__.__name__}(color={self.color})"
class Circle(Shape):
     
     """
    Class representing a circle.
    attributes:
    radius (float): The radius of the circle.
    """
     def __init__(self,radius:float,color:str="blue"):
        super().__init__(color)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
     def area(self) -> float:
        return pi * self.radius ** 2
     def perimeter(self) -> float:
        return 2 * pi * self.radius
     def __str__(self) -> str:
        return f"Circle(radius={self.radius}, color={self.color})"
class Rectangle(Shape):
      """
    Class representing a rectangle.
    Attributes"
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    """
      def __init__(self, width: float, height: float, color: str = "blue"):
       super().__init__(color)
       if width <=0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
       self.width = width
       self.height = height
      def area(self) -> float:
        return self.width * self.height
      def perimeter(self) -> float:
         return 2 * (self.width + self.height)
      def __str__(self) -> str:
            return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"
class Triangle(Shape):
     """
    Class representing a triangle. by the lenght of its three sides.
    attributes:
    x (float): The length of the first side.
    y (float): The length of the second side.
    z (float): The length of the third side.
    """
     def __init__(self, x: float, y: float, z: float, color: str = "blue"):
        super().__init__(color)
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("All sides must be positive numbers.")
        if x + y <= z or x + z <= y or y + z <= x:
            raise ValueError("The sum of the lengths of any two sides must be greater than the length of the third side.")
        self.x = x
        self.y = y
        self.z = z
     def area(self) -> float:
             surface = self.perimeter() / 2
             return sqrt(surface * (surface - self.x) * (surface - self.y) * (surface - self.z))
     def perimeter(self) -> float:
            return self.x + self.y + self.z
     def __str__(self) -> str:
            return f"Triangle(x={self.x}, y={self.y}, z={self.z}, color={self.color})"