# define a static variable and access that through a instance.
class Myclass:
    static_a = 15  # Static variable

obj = Myclass()
print(obj.static_a)