print("Welcome to income tax computation program ")
income = int(input("Enter your income (THB  ): "))
if 50001 < income < 100000:
    tax = 0.075 * income
    tax = float(tax)
    print("Tax expense = %d THB" % tax)
    net = income - tax
    print("Your net income after tax = %d THB" % net)
elif income > 100000:
    tax = 0.1 * income
    tax = float(tax)
    print("Tax expense = %d THB" % tax)
    net = income - tax
    print("Your net income after tax = %d THB" % net)
