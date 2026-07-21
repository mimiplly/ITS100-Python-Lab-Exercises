#ITS100 Lecture5 Repetition Structure: For Loops Lab5.6
for i in range (1,6):
    num = int(input("Enter a number between 1 and 20: "))
    if num <= 20 and num >= 1:
        if num % 2 == 0:
            print("%d is an even number." % num)
        elif num % 2 != 0:
            print("%d is an odd number." % num)
    else:
        print("number is invalid.")