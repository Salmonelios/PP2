animals = ["cat", "dog", "zuzalica", "mouse", "monkey"]
aboba = []

for x in animals:
    if "a" in x:
        aboba.append(x)
        
print(aboba)

abobaba = [x for x in animals if "o" in x]
print(abobaba)

y = int(input())
print(y)