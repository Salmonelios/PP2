import math

class Point:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    def show(self):
        return self.c1, self.c2
    def move(self, c11, c22):
        self.c1 = c11
        self.c2 = c22
    def dist(self, pointt):
        return math.sqrt((self.c1 - pointt.c1)**2 + (self.c2 - pointt.c2)**2)
    
point1 = Point(4, 3)
point2 = Point(0, 0)
print(point1.show())
print(point2.show())
point2.move(2, 5)
print(point2.show())
print(point1.dist(point2))