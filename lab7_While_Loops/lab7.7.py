#ITS100 Lecture7 While Loops Lab7.7

#Output:

# ===================
# Cashier Program
# ===================
# Enter item price or -1 when finished: 30.25
# Enter item price or -1 when finished: 18
# Enter item price or -1 when finished: 72
# Enter item price or -1 when finished: 24
# Enter item price or -1 when finished: 9
# Enter item price or -1 when finished: -1
# Total purchase amount is 153.25
# Your payment: 200
# You bought 5 items today.
# Your change is 46.75 baht.
print("===================")
print("Cashier Program")
print("===================")
l = []
while True:
    n = float(input(("Enter item price or -1 when finished: ")))
    if n == -1:
        break
    else:
        l.append(n)
print(f"TOtal amount is {sum(l)}")
pay = int(input("Your payment: "))
print(f"You bought {len(l)} items today.")
print(f"Your change is {pay-sum(l)}")