import os 
os.system('cls')

num=int(input("How Many Elements You Want to Add:"))
li=[]
for i in range(0,num):
    n=int(input("Enter Number:"))
    li.append(n)

print("Original List:",li)
lai=list(filter(lambda x:x>0,li))
print("Filtered List:",list(lai))