class Box :
    def __init__(self,weight) :
        self.weight = weight
        
    def __add__(self,other) :
        return self.weight + other.weight
b1 = Box(10)
b2 = Box(20)
print(b1+b2)
