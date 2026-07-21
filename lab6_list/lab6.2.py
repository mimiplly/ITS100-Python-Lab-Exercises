#ITS100 Lecture6 Lists Lab6.2
n = input("enter a comma-seperated list: ").split(",")
if len(n) >= 3:
    if len(n) == 3:
        print(*n)
    else:
        for i in n:
            for j in n:
                for k in n:
                    if i<j<k:
                        print(i,j,k)
