# Write a program to check whether a file is having read access and write access permissions.
import os
file_name="example.txt"
if os.access(file_name,os.R_OK):
    print("File has read Access")
else:
    print("File has no read Access")
if os.access(file_name,os.W_OK):
    print("File has Write Access")
else:
    print("File has no Write Access")
