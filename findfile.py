import os

f=os.listdir()
file_type=[]

for i in f:
    if i.endswith(".py"):
        file_type.append(i)

print("Python files:", file_type)