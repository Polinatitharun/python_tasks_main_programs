# Write a program to read a file stream supports random access.
with open("Example.txt", "r") as file:
    file.seek(5)  
    content = file.read(10)  
    print(content)