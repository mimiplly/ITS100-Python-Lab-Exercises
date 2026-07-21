#ITS100 Lecture2 Variables Input Output Lab2.3
r = input("Input Radius (cm): ")
h = input("Input Height (cm): ")
r, h = float(r), float(h)
volume = (3.14 * r**2 * h)
print("The volume of cylinder is %.5f cubic centimeters." %volume)