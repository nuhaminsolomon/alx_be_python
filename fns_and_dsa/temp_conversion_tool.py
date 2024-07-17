# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_DIFFERENCE = 32


# Implement Conversion Functions
def convert_to_CELSIUS_TO_(FAHRENHEIT):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_DIFFERENCE
    return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_FAHRENHEIT_TO_(CELSIUS):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_DIFFERENCE
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE
