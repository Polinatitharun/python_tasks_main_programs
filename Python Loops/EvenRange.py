# Write a program to print Even Number between the given range.
start=int(input())
end=int(input())
i=1
while(start<=end):
    if(start%2==0):
        print(start)
    start+=1
