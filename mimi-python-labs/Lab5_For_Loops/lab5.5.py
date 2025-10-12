lines =  int(input("enter no. of lines: "))
for i in range (1, lines + 1):
    if i % 2 == 0:
        print("*" * i)
    elif i % 2 != 0:
        print("-" * i)

