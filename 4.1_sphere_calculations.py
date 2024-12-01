import math 

radius = float(input("Enter the radius of the sphere: "))

diameter = 2 * radius

surface_area = 4 * math.pi * radius**2

volume = (4/3) * math.pi * radius**3

print(f"The diameter of the sphere is: {diameter}")
print(f"The surface area of the sphere is: {surface_area}")
print(f"The volume of the sphere is: {volume}")
