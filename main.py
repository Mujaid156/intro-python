_PI = 3.14
radius = int(input("Please enter the radius: "))
area = _PI * radius**2
print("The area of a circle is: " + str(area))


diameter = 2 * radius
print("The diameter of a circle is: " + str(diameter))

circumference = 2 * (_PI + radius)
print("The circumference of the circle is: " + str(circumference))
