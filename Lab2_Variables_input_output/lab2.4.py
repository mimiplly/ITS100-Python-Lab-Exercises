#ITS100 Lecture2 Variables Input Output Lab2.4
full = input("Input Full Score = ")
real = input("Input Real Score = ")
print(" --------------")
print(" --- Calculate Percentage --- ")
print(" --------------")
print(f"Full Score: {full}")
print(f"Real Score: {real}")
full, real = float(full), float(real)
percentage = (real / full) * 100
print("percentage:%.2f" %percentage)