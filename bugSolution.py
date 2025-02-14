def function_with_uncommon_error(x, y):
    try:
        if isinstance(y,(int,float)) and y!=0:
            result = x / y
            return result
        else:
            print("Error: Invalid input type or division by zero")
            return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)
print(result1)  # Output: 5.0

result2 = function_with_uncommon_error(10, 0)
print(result2)  # Output: Error: Invalid input type or division by zero
None

result3 = function_with_uncommon_error(10, "a")
print(result3)  # Output: Error: Invalid input type
None