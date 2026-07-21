#ITS100 Lecture7 While Loops Lab7.8

#Output:

# Enter an integer (0 to exit): 4
# Enter an integer (0 to exit): -5
# Enter an integer (0 to exit): 16
# Enter an integer (0 to exit): -8
# Enter an integer (0 to exit): 0
# ----------------------------------
# The number of even integers is 3
# The number of odd integers is 1

even = []
odd = []
while True:
    n = int(input("Enter an integer (0 to exit): "))
    if n == 0:
        break
    elif n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("----------------------------")
print(f"The number of even integer is {len(even)}")
print(f"The number of odd integer is {len(odd)}")