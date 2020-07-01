# Create a new program that will ask the user for the information
# needed to find the area of a trapezoid, and then print the area.

print("Area of Trapezoid")
print("-----------------")
length_1 = float(input("Enter first side: "))
length_2 = float(input("Enter second side: "))
height = float(input("Enter height: "))

area_trapezoid = ((length_1 + length_2) * height)/2
print("The area of trapezoid is: ", area_trapezoid)
