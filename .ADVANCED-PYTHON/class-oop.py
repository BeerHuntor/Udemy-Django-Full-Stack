class Circle():

    pi = 3.14

    def __init__(self, radius=2):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*self.pi
    
    def perimeter(self):
        return 2*self.pi*self.radius


c1 = Circle(radius=4)
print(c1.area())
print(c1.perimeter())