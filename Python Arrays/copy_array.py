# Write a function to copy an array to another array.
arr = list(map(int, input().split()))
copy_arr = []
for num in arr:
    copy_arr.append(num)
print(copy_arr)