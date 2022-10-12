import os
os.system('cls')

str1="Lorem Number Lorem ipsum dolor sit amet, consectetur adipiscing else 2002 2003  Lorem Ipsum ipsum dolor sit amet, consectetur adipiscing else 2003 2004"

lst=list(filter(lambda x:True if x in "0123456789" else False,str1))
print(lst)