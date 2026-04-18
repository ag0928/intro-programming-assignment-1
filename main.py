import shapes

print("Choose Shape:")
print("1-Circle")
print("2-Rectangle")
print("3-Triangle")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle =", shapes.circle_area(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle =", shapes.rectangle_area(l, w))

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle =", shapes.triangle_area(b, h))

else:
    print("Invalid choice")
