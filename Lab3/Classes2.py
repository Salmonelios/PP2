class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__()
        self.length = lenght
        self.wigth = width
    def area(self):
        return self.length * self.wigth

leen = Square(12)
print(leen.area())
Priamougolnik = Rectangle(3, 4)
print(Priamougolnik.area())