# Write a function to calculate the average value of an array of integers.
def average_array(arr):
    if len(arr)==0:
        return 0
    return sum(arr)/len(arr)
n=int(input("Enter No. of Elements of an array"))
arr=[]
for i in range(n):
    num=int(input("Enter Elements"))#elements
    arr.append(num)
average=average_array(arr)
print("Average of an Array:",average)
