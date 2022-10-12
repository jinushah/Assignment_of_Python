import os
os.system('cls')

lose=[]
num1=int(input("How Many Elements You Want to Add:"))

for i in range(0,num1):
    num=int(input("Enter Number:"))
    lose.append(num)

lst=list(filter(lambda x:x%2==0,lose))
lst2=list(filter(lambda x:x%2!=0,lose))

print("Even List:",list(lst))
print("Odd List:",list(lst2))