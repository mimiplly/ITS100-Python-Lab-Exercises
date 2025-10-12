print("====RESTART====")
service =input("Choose your service: W=Wash C=Wash+Vacuum: ")
service = service.upper()
if service == "W":
    size = input('Enter your car size: "S" "M" "L":')
    size = size.upper()
    if size == "S":
        price = 100
    elif size == "M":
        price = 150
    elif size == "L":
        price = 200
    else:
        print("You entered an invalid size")

elif service == "C":
    size = input('Enter your car size: "S" "M" "L": ')
    size = size.upper()
    if size == "S":
        price = 150
    elif size == "M":
        price = 200
    elif size == "L":
        price = 250
    else:
        print("You entered an invalid size")
else:
    print("You entered an invalid service")