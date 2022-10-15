import os
from tokenize import String
os.system('cls')

lose=[]
string = ""
num1=int(input("How Many Elements You Want to Add:"))

for i in range(0,num1):
   num=input("Enter String:")
   string += num
   
# print(string)
lose = list(string)

lst=list(filter(lambda x:True if x.lower() in "aeiou" else False, lose))

print(lst)
