class Calculator:
  """
  This class represents a Calculator with static and class methods.
  """
  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Static method that performs addition of two numbers.

    Args:
      a (int or float): First number.
      b (int or float): Second number.

    Returns:
      int or float: The sum of a and b.
    """
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Class method that performs multiplication of two numbers.

    Args:
      cls (class): The Calculator class itself.
      a (int or float): First number.
      b (int or float): Second number.

    Returns:
      int or float: The product of a and b.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b

# This part is for testing purposes and not included in class_static_methods_demo.py
if __name__ == "__main__":
  # Using the static method
  sum_result = Calculator.add(10, 5)
  print(f"The sum is: {sum_result}")

  # Using the class method
  product_result = Calculator.multiply(10, 5)
  print(f"The product is: {product_result}")