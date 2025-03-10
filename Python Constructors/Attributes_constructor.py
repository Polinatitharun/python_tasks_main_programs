# Write a program which illustrates the concept of attributes of a constructor.

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
        print(f"Person Created: {self.name}, {self.age} years old")

if __name__ == "__main__":
    obj = Person("Divya", 20)
    print(f"Name: {obj.name}, Age: {obj.age}")