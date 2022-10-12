import os
os.system('cls')

s=input("Enter String:")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)

print(l)