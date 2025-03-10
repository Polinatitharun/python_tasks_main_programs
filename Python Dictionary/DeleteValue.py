# Delete a value from a Dictionary
students={1:'Amrutha',2:'Divya',3:'Prasad',4:'Ram',5:'Chandu'}
n=int(input("Enter Rollno to delete a value"))
del students[n]
print("Dictionary After Deletion Operation",students)