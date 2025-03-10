# create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods.
from Abstract_Class import AbstractClass

class ChildClass(AbstractClass):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

    def abstract_method(self):
        print("Implementation of abstract method in ChildClass")

if __name__ == "__main__":
    obj = ChildClass()
    obj.non_abstract_method()