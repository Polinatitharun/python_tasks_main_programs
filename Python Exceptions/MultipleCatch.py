# write a program with multiple catch blocks.

try:
    num1 = 10
    num2 = 0
    x=int("Python")
    result = num1 / num2  
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Occur vaueError.")