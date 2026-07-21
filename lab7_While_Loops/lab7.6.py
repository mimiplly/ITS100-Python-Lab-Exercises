#ITS100 Lecture7 While Loops Lab7.6

#Output:
# ===== MAIN MENU =====
    # 1. Addition
    # 2. Subtraction
    # 3. Exit
    # Select an operation (1-3): 1
    # Enter two numbers: 12 20
    # 12 + 20 = 32

    # ===== MAIN MENU =====
    # 1. Addition
    # 2. Subtraction
    # 3. Exit
    # Select an operation (1-3): 2
    # Enter two numbers: 12 20
    # 12 - 10 = 2

    # ===== MAIN MENU =====
    # 1. Addition
    # 2. Subtraction
    # 3. Exit
    # Select an operation (1-3): 3
    # Bye!!!

while True:
    print("===== MAIN MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    print("")
    n = int(input("Select an operation (1-3): "))
    if n == 3:
        print("Bye!!!")
        exit()
    elif  n == 1:
        hehe = input("Enter two numbers: ").split(" ")
        a = hehe[0]
        b = hehe[1]
        sum = int(a)+int(b)
        print(f"{a}+{b}={sum}")
        
