#Abylkassym Aruzhan
#laboratory work 2
#Here we will compare 3 numbers and dfind minimum in 3 of them
print("enter 1st number: ")
a = int(input()) 
print("enter 2nd number: ")
b = int(input())
print("enter 3rd number: ")
c = int(input())
if b >= a <= c:
    print(a,"this number is the minimum")
elif a >= b <= c:
    print(b,"this number is the minimum")
else:
    print(c, "this number is the minimum")