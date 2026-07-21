#ITS100 Lecture5 Repetition Structure: For Loops Lab5.4
integer = int(input("Enter an integer (n>0): "))
print(" (1) Factorial of n (n!)")
print(" (2) Sum of integers from 1 to n")
choice = int(input("Please enter your choice: "))
if choice == 1:
    factorial = 1
    for i in range (1, 1 + integer):
        factorial *= i
    print("The factorial of %d is %d." % (integer, factorial))  
elif choice == 2:
    sum = 0
    for i in range(1, integer +1):
        sum += i
    print("The sum of integers from 1 to %d is %d." % (integer, sum))
