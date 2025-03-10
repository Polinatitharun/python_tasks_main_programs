# write a program with finally block.

try:
    10/0
    print("Inside try block")
except ZeroDivisionError:
    print("Exception caught!")
finally:
    print("This will always execute.")