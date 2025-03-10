# Handle the Arithmetic Exception using try-catch block.

try:
    m=10
    n=0
    result=m/n
    print(result)
except ZeroDivisionError:
    print("Error:Can't perform Division by Zero")