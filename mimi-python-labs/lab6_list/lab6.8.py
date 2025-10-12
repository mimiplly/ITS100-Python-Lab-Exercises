n = input("enter a string: ")
list = []
for i in n:
    if i.isupper():
        i = i.lower()
        list.append(i)
    elif i.islower():
        i = i.upper()
        list.append(i)
    else:
        list.append(i)
print("reverse string output: ",end="")
for i in list: ###
    print(i,end="") ##