# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            result = num1 / num2
    else:
        return "Error: Invalid operation"
    return result

if __name__ == "__main__":
    # This block will only execute if this script is run directly
    print("This is the arithmetic_operations module.")
    print("Import this module and use the perform_operation function in main.py.")