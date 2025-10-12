n = input("enter a comma seperated list: ").split(',')
for i in range(len(n)):
    for j in range(len(n)):
        for k in range(len(n)):
            if i != j and j != k and i != k:
                print(n[i],n[j],n[k])
