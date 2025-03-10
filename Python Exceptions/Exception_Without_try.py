# Write a method which throws an exception, call that method in main class without try block.
def divideNumbers(a,b):
    if b==0:
        raise ZeroDivisionError("Can't Perform Division by Zero")
    return a/b
def main():
    result=divideNumbers(10,0)
    print(result)
main()