# write a program to read a file a just to a particular index using seek()
with open("Example.txt", "r") as file:
    file.seek(10)
    print(file.read(5))