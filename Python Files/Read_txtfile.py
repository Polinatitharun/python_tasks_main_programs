# Write a program to read text file.
with open("python.txt", "r") as file:
    content = file.read()
    print(content)