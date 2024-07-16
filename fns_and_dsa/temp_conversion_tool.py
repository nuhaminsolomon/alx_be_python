# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_DIFFERENCE = 32


# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius factor . 
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_DIFFERENCE
    return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit factor .
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_DIFFERENCE
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE

# User Interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if name == "main":
    main()
