#Write a program to read file stream.
with open("Example.txt","r")as file:
    for line in file:
        print(line.strip())