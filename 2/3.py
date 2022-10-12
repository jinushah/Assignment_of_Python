import os
os.system('cls')

str1="Lorem ipsum dolor sit amet, consectetur adip"

# for i in range(0,num1):
#     board=input("Enter String:")
#     lose.append(board)

lst=list(filter(lambda x:True if x.lower() in "aeiou" else False, str1))

print(lst)
