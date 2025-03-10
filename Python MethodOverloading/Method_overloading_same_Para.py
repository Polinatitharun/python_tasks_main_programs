# Write two methods with the same name and same number of parameters of same type.
class Myclass():
    def show(self,a,b):
        print("First Method:",a+b)
    def show(self,a,b):
        print("Second Method:",a*b)
obj=Myclass()
obj.show(10,20)