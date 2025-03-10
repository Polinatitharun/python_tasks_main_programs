# Write two methods with the same name but different number of parameters of same type and call the methods.

class Myclass:
    def add(self, a,b=0):
        return a+b
obj=Myclass()
print("Addition with one parameter: ",obj.add(10))
print("Addition with two parameters: ",obj.add(10,20))