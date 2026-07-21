#ITS100 Lecture2 Variables Input Output Lab2.7
weight = input("Input Weight (kg): ")
height = input("Input Height (m): ")
weight, height = float(weight), float(height)
pounds = weight * 2.20462
feet = height * 3.28084
print("Weight in pounds: %.2f" % pounds)
print("Height in feet: %.2f" % feet)
bmi = pounds / (feet ** 2)
print("BMI: %.2f" % bmi)
