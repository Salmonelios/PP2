car = ("Porshe",)
print(type(car))

Roman = ("kotletki", "s", "pureshka", "compot")
y = list(Roman)
y.remove("compot")
Roman = tuple(y)
print(Roman)
Roma = ("Chai",)
Romario = Roman + Roma
print(Romario)

*u, i = Roman
print(u, i)

print([x for x in Roman])
Roman *= 2
print(Roman)