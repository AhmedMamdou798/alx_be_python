# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius using the global factor."""
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit using the global factor."""
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    while True:
        try:
            temperature_str = input("Enter the temperature to convert: ")
            temperature = float(temperature_str)  # Attempt to convert immediately for initial validation
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                celsius = convert_to_celsius(temperature)
                print(f"{temperature}°F is {celsius}°C")
                break
            elif unit == 'C':
                fahrenheit = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {fahrenheit}°F")
                break
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")