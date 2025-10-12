while True:
    n = int(input("Enter an integer number: "))
    if n <= 0 or n > 10:
        print("1 - 10 !!!!")
    else:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()

        for l in range(n-1, -1, -1):
            for k in range(1, l+1):
                print(k, end=" ")
            print()
        break