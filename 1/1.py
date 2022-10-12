import os
os.system('cls')

num=[1,2,3,4,5,6,7,8,9]
print("Original Lists:",num)
result=map(lambda x:x+x+x,num)
print("\nTriple of said list numbers:")
print(tuple(result))


