import math

# Shape.py
def circle_area(r):
    return math.pi * r * r

def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

# Main.py
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area:", circle_area(r))
elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", rectangle_area(l, w))
elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", triangle_area(b, h))
else:
    print("Invalid choice")
