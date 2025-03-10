# Program to access the values of nested dictionary.
students={
    1:{'Name':'Divya','Branch':'BCA'},
    2:{'Name':'Amrutha','Branch':'BSC'},
    3:{'Name':'Prasad','Branch':'MCA'},
    4:{'Name':'Ram','Branch':'Bcom'},
    5:{'Name':'Chandu','Branch':'Btech'}
}
n=int(input("Enter Roll_no"))
print("Name of student:",students[n]['Name'])
print("Branch: ",students[n]['Branch'])
