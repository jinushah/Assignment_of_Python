import os
os.system('cls')

num1=[]
num2=[]

n=int(input("How Many Elements You Want to Add in List 1:"))

for i in range(0,n):
    number=int(input("Enter a Number:"))
    num1.append(number)

y=int(input("How Many Elements You Want to Add in List 2:"))

for i in range(0,y):
    numbers=int(input("Enter a Number:"))
    num2.append(numbers)

result=map(lambda x,y:x+y,num1,num2)
print("Result of Adding 2 List:",list(result))
