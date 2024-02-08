def to_ounces(a):
    return a * 28.3495231
def to_Cel(a):
    return (a-32)*5/9
def solve(heads, legs):
    t = legs - heads*2
    t /=2
    c = heads - t
    print("Rabbits:", int(t), "Chickens:", int(c))
def filter_prime(lis):
    nee = []
    for i in lis:
        u = True
        for n in range(2, i):
            if i%n == 0:
                u = False
        if u:
            nee.append(i)
    return nee

print(to_ounces(321))
print(to_Cel(42))
solve(35, 94)
print(filter_prime([1, 2,3 ,4, 5,6 , 7, 8, 9, 10, 11]))