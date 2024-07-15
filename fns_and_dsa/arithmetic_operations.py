#
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float: The result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
