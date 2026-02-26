class Shape:
    def draw(self):
        print("Drawing a Shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")


# Create objects
c = Circle()
r = Rectangle()

# Polymorphism demonstration
c.draw()
r.draw()
