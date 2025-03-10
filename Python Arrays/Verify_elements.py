# write a method to verify if the array contains two specified elements.
arr = list(map(int, input().split()))
elements = list(map(int, input().split()))
found = True
for num in elements:
    if num not in arr:
        found = False
        break
print(found)