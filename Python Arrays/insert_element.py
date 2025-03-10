# write a function to insert an element at a specific position in the array.
arr = list(map(int, input().split()))
element = int(input())
position = int(input())
new_arr = arr[:position] + [element] + arr[position:]
print(new_arr)