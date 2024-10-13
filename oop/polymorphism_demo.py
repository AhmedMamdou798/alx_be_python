from math import pi

class Shape:
  """
  This class represents a base Shape object.
  """
  def area(self):
    """
    Raises a NotImplementedError as derived classes must implement this method.
    """
    raise NotImplementedError("Area calculation not implemented for base Shape")

class Rectangle(Shape):
  """
  This class represents a Rectangle derived from Shape.
  """
  def __init__(self, length, width):
    """
    Initializes a Rectangle with length and width.

    Args:
      length (float): The length of the rectangle.
      width (float): The width of the rectangle.
    """
    self.length = length
    self.width = width

  def area(self):
    """
    Calculates and returns the area of the rectangle.

    Returns:
      float: The area of the rectangle (length * width).
    """
    return self.length * self.width

class Circle(Shape):
  """
  This class represents a Circle derived from Shape.
  """
  def __init__(self, radius):
    """
    Initializes a Circle with radius.

    Args:
      radius (float): The radius of the circle.
    """
    self.radius = radius

  def area(self):
    """
    Calculates and returns the area of the circle.

    Returns:
      float: The area of the circle (pi * radius^2).
    """
    return pi * self.radius** 2

# This part is for testing purposes and not included in polymorphism_demo.py
if __name__ == "__main__":
  shapes = [
      Rectangle(10, 5),
      Circle(7)
  ]

  for shape in shapes:
      print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")