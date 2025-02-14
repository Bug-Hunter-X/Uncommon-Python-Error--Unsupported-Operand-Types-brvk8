# Uncommon Python Error: Unsupported Operand Types

This repository demonstrates a scenario where an uncommon error occurs in Python: handling unsupported operand types for the division operator (/).

The `bug.py` file contains a function that showcases this error. It attempts to divide an integer by a string, which is not a valid operation in Python. The code includes error handling using `try-except` blocks, catching both `ZeroDivisionError` and `TypeError` exceptions.

The `bugSolution.py` file is empty, since the bug is in the handling of the exception. The solution would involve appropriate input validation to prevent such cases.