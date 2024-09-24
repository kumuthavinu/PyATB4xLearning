# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

import math

radius = float(input("Please Enter the Radius of the Circle : "))
print(radius)
area = 3.14 * (radius**2)
print(f"Area of the Circle is : {area:.3f}")
