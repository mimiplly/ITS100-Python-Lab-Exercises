n = int(input("how many persons in a group?: "))
list = []
for i in "ABC":
    print(f"please enter grade from group {i}")
    for j in range(n):
        grade = float(input("enter grade: "))
        list.append(grade)

lista = list[:n]
listb = list[n:n*2]
listc = list[n*2:n*4]

print("the highest grade of group A is",max(lista))
print("the highest grade of group B is",max(listb))
print("the highest grade of group C is",max(listc))
