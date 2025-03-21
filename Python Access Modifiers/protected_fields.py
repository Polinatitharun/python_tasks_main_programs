class A:
    def __init__(self):
        self._protected_var = "Protected Variable"

    def _protected_method(self):
        print("This is a protected method")

class B(A):
    def access_protected(self):
        print(self._protected_var)  
        self._protected_method()    

if __name__ == "__main__":
    objA = A()
    print(objA._protected_var)  
    objA._protected_method()    

    objB = B()
    objB.access_protected()   