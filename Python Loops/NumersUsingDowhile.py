# Write a program to print a numbers in range using do- while loop statement.
start=int(input("Enter Starting Number"))
end=int(input("Enter Ending Number"))
while True:
    print(start)
    start+=1
    if(start>end):
        break
