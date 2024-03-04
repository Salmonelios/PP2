with open('test.txt', 'r') as file:
    print(len(file.readlines()))
    
lsst = [3, 6, 9, 12, 15, "Tirolskii pirog"]

with open("test.txt", 'a') as file:
    for i in lsst:
        file.write('\n' + str(i))