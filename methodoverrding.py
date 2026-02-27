class vehicle :
        def move(self) :
                print("vehicle is moving")
                
class car(vehicle) :
        def move(self) :
                print("driving on the road")
class cycle(vehicle) :
        def move(self) :
                print("pedalling on the road")
c = car()
b = cycle()
c.move()
b.move()
