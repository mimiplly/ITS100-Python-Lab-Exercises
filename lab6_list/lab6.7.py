import random as r
list = []
for i in range(4):
    n = input(f"enter string #{i+1}:")
    list.append(n)
r.shuffle(list) ##
print(f"random order of sentence: ",*list)
