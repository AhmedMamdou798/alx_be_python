# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return float(num1) + float(num2)
    elif operation == 'subtract':
        return float(num1) - float(num2)
    elif operation == 'multiply':
        return float(num1) * float(num2)
    elif operation == 'divide':
        if float(num2) == 0:
            return "Error: Division by zero"
        else:
            return float(num1) / float(num2)
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    # This block will only execute if this script is run directly
    print("This is the arithmetic_operations module.")
    print("Import this module and use the perform_operation function in main.py.")