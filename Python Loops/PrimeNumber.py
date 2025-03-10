#Write a program to find the prime number or not.
N=int(input("Enter Number"))
c=0
i=1
while(i<=N):
    if(N%i==0):
        c+=1
    i+=1
if (c==2):
    print("Prime")
else:
    print("Not Prime")
