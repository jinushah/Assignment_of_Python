import os
os.system('cls')

lose=[]
num1=int(input("How Many Elements You Want to Add:"))

for i in range(0,num1):
   num=int(input("Enter Number:"))
   lose.append(num)

lst=list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, lose)))

print(lst)

