
from math import *
d = float(input("Enter the distance to the building: "))
r = float(input("Enter the elevation angle in degree: "))
h = d*tan(radians(r))
print("The building height is %.4f."%h)