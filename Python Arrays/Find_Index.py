# Write a program to find the index of an array element.
arr = list(map(int, input().split()))
target = int(input())
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break