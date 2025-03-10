# Write a program to remove the duplicate elements and return the new array.
arr = list(map(int, input().split()))
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)