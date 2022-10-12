import os
os.system('cls')

li=int(input("How Many Elements You Want To Add:"))
float_list=[]
for i in range(0,li):
    num=float(input("Enter Decimal Number:"))
    float_list.append(num)

print(list(map(int, float_list)))