def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)
print(result1)  # Output: 5.0

result2 = function_with_uncommon_error(10, 0)
print(result2)  # Output: Error: Division by zero
None

result3 = function_with_uncommon_error(10, "a")
print(result3)  # Output: Error: Unsupported operand type(s) for / 
None