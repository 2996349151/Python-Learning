class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def area(self):
        return self.length ** 2

class Circle(Shape):
    def __init__(self, radius):
        super().__init()__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

def area(x):
    return x.area()
