# Write a method to find the second largest number in an array.
arr = list(map(int, input().split()))
arr.sort()
print(arr[-2])