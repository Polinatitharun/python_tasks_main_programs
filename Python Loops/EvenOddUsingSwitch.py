# Write a program to check a number is EVEN or ODD using Switch

'''N=int(input())
match N % 2:
    case 1:
        print("Odd")
    case 2:
        print("Even")'''
N=int(input())
dicti={0:'EVEN',1:'ODD'}
print(dicti[N%2])