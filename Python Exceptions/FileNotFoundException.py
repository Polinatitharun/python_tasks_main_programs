# write a program to generate a FileNotFoundException.

try:
    fileopen=open("Python.doc","r")
except FileNotFoundError:
    print("File is not Found")