from   shapes import Circle,Rectangle,Triangle
def display():
    """
    Function to display the shapes and their properties.
    """
    # Creating a circle object
    cir= Circle(radius= 5,color="blue")
    rec= Rectangle(width=5,height=9,color="blue")
    tri= Triangle(x=5,y=6,z=7,color="blue")
    # Displaying the shape details
    shapes=[cir,rec,tri]
    for shape in shapes:
        print(f"Shape: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print('-'*20)
if __name__ == "__main__":
    display()