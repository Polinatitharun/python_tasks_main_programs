#Write a program to check Armstrong Number or NOt.
N=int(input("Enter a Number"))
temp=N
sum=0
while(N>0):
    remainder=N % 10
    sum=sum+(remainder*remainder*remainder)
    N=N//10
if(sum==temp):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")