mi=[]
for i in range(1,6):
    n = int(input(f"Input #{i}: "))
    mi.append(n)
result = input("select the opthin: 1)summary, 2)average, 3)min, 4)max...")
sum = sum(mi)
avr = sum/ 5
min = min(mi)
max = max(mi)

if result == '1':
    print(f"Your result is {sum}")
if result == '2':
    print(f"Your result is {avr}")
if result == '3':
    print(f"Your result is {min}")
if result == '4':
    print(f"Your result is {max}")
else:
    print("error")