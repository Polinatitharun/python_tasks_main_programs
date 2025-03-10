# Write a program to palindrome or not.

N=int(input("Enter a Number"))
temp=N
sum=0
while(N>0):
    rem=N%10
    sum=sum*10+rem
    N=N//10
if(sum==temp):
    print("Palindrome")
else:
    print("Not Palindrome")