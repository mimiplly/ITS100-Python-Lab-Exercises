#ITS100 Lecture7 While Loops Lab7.9

#Output:

# Enter an integer (-1 to exit): 8
# Enter an integer (-1 to exit): 7
# Enter an integer (-1 to exit): 5
# Enter an integer (-1 to exit): 2
# Enter an integer (-1 to exit): 3
# Enter an integer (-1 to exit): -1
# The sum of 5 number(s) is 24.

l = []
while True:
    n = int(input("Enter an integer (-1 to exit): "))
    if n == -1:
        break
    else:
        l.append(n)
print(f"The sum of {len(l)} number(s) is {sum(l)}")