# write two methods with the same name but different number of parameters of different type and call the methods.
class Myclass:
    def show(self, a, b=None):
        if b is None:
            print("Single parameter:",a)
        elif isinstance(a,int) and isinstance(b,str):
            print(f"Integer and string:{a} - {b}")
        elif isinstance(a,str)and isinstance(b,int):
            print(f"String and Integer: {a}-{b}")
        else:
            print("Different data types:",a,b)
obj=Myclass()
obj.show(10)
obj.show("Programming",20)
obj.show(20,"Programming")
