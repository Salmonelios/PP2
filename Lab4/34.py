def TCH(s):
    x = 0
    while s>x:
        if x%3==0 and x%4==0:
            yield x
        x += 1
        
num = TCH(100)

for i in num:
    print(i, end = " ")
    