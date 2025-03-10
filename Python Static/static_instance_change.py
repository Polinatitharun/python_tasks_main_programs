# define a static variable and change within the instance.
class Myclass:
    static_a = 15  # Static variable

obj1 = Myclass()
obj1.static_a = 30  # This creates an instance variable, not changing the class variable

print(Myclass.static_a)  # Still 10 (class variable remains unchanged)
print(obj1.static_a) 