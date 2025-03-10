# Apply private, public , protected and default access modifiers to the constructor.

class AccessModifiers:
    def __init__(self):  
        print("Public Constructor Called")

    def _protected_constructor(self):  
        print("Protected Constructor Called")

    def __private_constructor(self):  
        print("Private Constructor Called")

if __name__ == "__main__":
    obj = AccessModifiers()  
    obj._protected_constructor()
    
   # obj.__private_constructor()  #shows an error
