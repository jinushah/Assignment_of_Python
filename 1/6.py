import os 
import pandas as pd
os.system('cls')

num=int(input("Enter A Number:"))

result=list(map(lambda x,y:x*y,list(range(1,11)),[num]*10))

print(result)