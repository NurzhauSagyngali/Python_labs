import math

number_of_sides = int(input("Input number of sides: "))
length_of_a_side = float(input("Input the length of a side: "))
apothem = (length_of_a_side)/(2 *(math.tan(math.pi/number_of_sides)))

area_of_the_polygon = (number_of_sides * length_of_a_side * apothem)/2

print("The area of the polygon is:", int(area_of_the_polygon))