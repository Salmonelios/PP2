list = ["Nikita", "yes", True, 100, 4.0]
print(list)
print(len(list))
print(type(list))
print("\n")
print(list[2])
print(list[2:])
print("Nikita" in list)
print("\n")
list[1] = "no"
print(list)
list[:2] = ["roma", "Roma"]
print(list)
list[1:2] = ["Andrey", "Yarik"]
print(list)
list[1:3] = ["DA"]
print(list)
list.insert(3, "Cat")
print(list)
list.append(32)
print(list)
newlist = ["Dog", "yabloko", 54]
list.extend(newlist)
print(list)
list.remove(32)
print(list)
list.pop(2)
print(list)
del list[0]
print(list)
list.clear()
print(list)
del list
print(list)