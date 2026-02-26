class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(self.brand, self.model, self.year)


car1 = Car("audi", "A15", 2020)
car2 = Car("bmw", "Nord", 2025)

car1.display()
car2.display()
