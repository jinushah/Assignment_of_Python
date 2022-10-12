import os
os.system('cls')

def example(s):
    return s.lower()

tup_example =("THIS","IS","A","NUMBER")
upd_tup=map(example,tup_example)
print(tuple(upd_tup))
