from geometry import calculate_rectangle_area

length = 1012
width = 52333

# The following line will not raise any type-related errors during static type checking
area = calculate_rectangle_area(length, width)

print(f"The area of the rectangle is: {area}")


from typing import List

def li(arr: List[int | str]) -> int:
    for i in arr:
        return int((i))

new_li = li([1, 2, 3,4 ,5, "Ali", True])
print(new_li)
print(li.__annotations__)