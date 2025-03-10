# write a program to generate NoSuchFieldException.

class Person:
    def _init__(self):
        self.name = "name" 

obj=Person()

try:
    print(obj.age)# access non-existing Field
except AttributeError as e:
    print("Error: No such field exists in the object.")