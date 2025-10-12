n = input("enter dd/mm/yyyy: ")
if len(n) == 8:
    date = n[:2]
    month = n[2:4]
    year = n[4:]
    if int(month) > 12 or int(month) <0:
        print("there're 12 months")
    else:
        print(f"date = {date}")
        print(f"month = {month}")
        print(f"year = {year}")
else:
    print("please enter 8 digits!!")