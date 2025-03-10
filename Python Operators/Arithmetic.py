# Write a function for arithmetic operators(+,-,*,/).
def Arithmetic():
    sum=a+b
    difference=a-b
    product=a*b
    division=a/b
    return sum , difference,product,division
a=int(input())
b=int(input())
c=Arithmetic()
print(c)
