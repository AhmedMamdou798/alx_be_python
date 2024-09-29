def perform_operation(num1: float, num2: float, operation: str) -> float:
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: First number (float).
      num2: Second number (float).
      operation: String specifying the operation to perform ('add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the arithmetic operation (float) or a special value for division by zero.
  """

  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return float('nan')  # Special value for division by zero (Not a Number)
    else:
      return num1 / num2
  else:
    raise ValueError("Invalid operation provided. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")