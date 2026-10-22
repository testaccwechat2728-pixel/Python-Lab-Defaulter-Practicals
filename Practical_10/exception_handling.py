"""
Practical No. 10: Built-in Exception Handling in Python
Demonstrates handling ZeroDivisionError, TypeError, ValueError, and generic Exception.
"""

def divide_numbers(num1, num2):
    """
    Divides num1 by num2 with comprehensive exception handling:
    - ZeroDivisionError: dividing by 0
    - TypeError: incompatible input types
    - ValueError: invalid numeric string/value
    - Exception: any other unforeseen runtime exceptions
    """
    try:
        # Input validation for type mismatch and value errors
        if isinstance(num1, str) and not num1.replace('.', '', 1).isdigit():
            raise TypeError("Invalid input type. Please enter numbers only.")
        if isinstance(num2, str) and not num2.replace('.', '', 1).isdigit():
            raise ValueError("Invalid input value. Please enter a valid number.")
        if num1 is None or num2 is None:
            raise Exception("unsupported operand type(s) for /: 'int' and 'NoneType'")

        # Attempt division
        result = num1 / num2
        print(f"The result is: {result}")
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero!")
    except TypeError:
        # Handle type mismatch error
        print("Error: Invalid input type. Please enter numbers only.")
    except ValueError:
        # Handle value error (e.g., trying to divide by a string)
        print("Error: Invalid input value. Please enter a valid number.")
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

def main():
    # Test the function with valid inputs
    print("Test 1: Valid inputs")
    divide_numbers(10, 2)

    # Test the function with division by zero
    print("\nTest 2: Division by zero")
    divide_numbers(10, 0)

    # Test the function with invalid input types
    print("\nTest 3: Invalid input types")
    divide_numbers("ten", 2)

    # Test the function with value error
    print("\nTest 4: Value error")
    divide_numbers(10, "two")

    # Test the function with unexpected exception
    print("\nTest 5: Unexpected exception")
    divide_numbers(10, None)

if __name__ == "__main__":
    main()
