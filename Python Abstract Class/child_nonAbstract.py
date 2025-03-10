# Create an instance for the child class in child class and call non abstract methods.
from Sub_class import ChildClass

if __name__ == "__main__":
    obj = ChildClass()
    obj.non_abstract_method()