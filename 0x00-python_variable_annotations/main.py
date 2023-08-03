from geometry import calculate_rectangle_area

length = 10.5
width = 5.2

# The following line will not raise any type-related errors during static type checking
area = calculate_rectangle_area(length, width)

print(f"The area of the rectangle is: {area}")