fruit = input("list of fruits:").split(",")
for i in fruit:
    if len(i) < 6:
        print(f"{i} is only {len(i)} long")
    elif len(i) >= 6:
        print(f"{i} is {len(i)} characters or more!")