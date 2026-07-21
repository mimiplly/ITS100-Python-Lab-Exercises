#ITS100 Lecture6 Lists Lab6.9
##REVIEW
a = input("a = ").split(" ")
b = input("b = ").split(" ")
x = a+b
list = []
for i in x:
    if x.count(i) > 1:
        i = int(i)
        list.append(i)
        for j in list:
            if list.count(j) != 1:
                list.remove(j)
print(list)

        
    