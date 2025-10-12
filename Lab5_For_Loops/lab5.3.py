print("Multiplication table:)")
num = int(input(("Plese enter a number between 1 to  25:")))
if num < 1 or num > 25:
    print("Invalid number. Please enter a number between 1 and 25.")
else:
    print("Multiplication table of %d." %num)
for i in range(1, 13):
    print("%d x %d = %d" %(num, i, num*i))

          