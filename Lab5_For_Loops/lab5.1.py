
even = 0
odd = 0
for i in range(1,6):
    num = int(input("Enter a number: "))
    if num %2 == 0:
        even += 1
    elif num % 2 != 0:
        odd += 1
print("there were %d even numbbers." % even)
print("there were %d odd numbers." % odd)