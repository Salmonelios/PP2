def sg(s):
    x = 1
    while s>=x:
        yield x**2
        x += 1
            
for i in sg(15):
    print(i, end = " ")