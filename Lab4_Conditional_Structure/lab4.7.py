#ITS100 Lecture4 Conditional Structure Lab4.7
have = int(input("enter money you have: "))
item = int(input("enter price of item: "))
tax = 0.08 * item
print("Tax : %d" %tax)
total = item + tax
if have >= total:
    print("You can buy this item.")
else:
    print("You cannot buy this item.")
    print("You need %d more." % (total - have))