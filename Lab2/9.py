dic = {
    1 : "PP",
    2 : "Discra",
    3 : "Stata",
    4 : "Calculus"
}
print(dic)
k = dic.keys()
print(k)
dic[5] = "MPGE"
print(k)
print(dic.values())
print(dic.items())
dic.update({4:"Calculus2"})
print(dic)
dic.popitem()
print(dic)
for x, y in dic.items():
    print(x, y)