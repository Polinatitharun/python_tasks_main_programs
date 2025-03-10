# Define the local and global variables with the same name and print both variables and the scope of the variables.
a=5
def scope():
    a=10
    print("Local Variable: ",a)
scope()
print("Global Variable: ",a)
