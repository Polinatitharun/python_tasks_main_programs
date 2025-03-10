# write a class with a default constuctor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class.

class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print(f"One-Argument Constructor Called: a = {a}")
        else:
            print(f"Two-Argument Constructor Called: a = {a}, b = {b}")

if __name__ == "__main__":
    obj1 = MyClass()         
    obj2 = MyClass(10)      
    obj3 = MyClass(10, 20)   