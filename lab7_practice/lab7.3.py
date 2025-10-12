n = int(input("Enter an integer number:"))
i = 0
while i < n:
    j = 0
    while j < n:
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("o",end=" ")
        elif j >= i:
            print("x",end = " ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1