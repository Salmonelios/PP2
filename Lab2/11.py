a = 90
b = 10
print("da") if a>b else print("net") if a==b else print("navernoe")

if 5>4 and 5<6:
    print(1)
    
if 5>4 or 600<1:
    print(423)
    
if a>b:
    pass
else:
    print(9+9)
    
while b>0:
    b-=1
    if b == 5:
        continue
    print(b)
    
for x in range(11):
    if x == 3:
        break
    print(x)