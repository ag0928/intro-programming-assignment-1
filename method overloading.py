class calculator : 
    def add(self,a,b=0,c=0) : 
        return a+b+c
c=calculator()
print(c.add(10))
print(c.add(10,30))
print(c.add(10,20,30))
