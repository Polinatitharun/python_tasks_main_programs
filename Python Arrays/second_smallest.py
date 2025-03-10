# write a program to find the second smallest number in an array.
arr = list(map(int, input().split()))
arr = list(set(arr))  # Remove duplicates
arr.sort()
print(arr[1])