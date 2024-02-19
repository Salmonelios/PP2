import math

y = int(input("Write angle in degree: "))
print("In radiad:", y/180*math.pi)

h = int(input("Write height: "))
b1 = int(input("Write first base: "))
b2 = int(input("Write second base: "))
print("The area is:", (b1+b2)/2*h)

s = int(input("Write a number of sides: "))
lenght = int(input("Write lenght of a side: "))
print("The area is:", (1/4)*(lenght*lenght*s)/math.tan(math.pi/s))

f = int(input("Write a length of base: "))
g = int(input("Write a height: "))
print("The area is:", f*g)