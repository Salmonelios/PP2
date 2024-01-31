Dolma = [x for x in range(10)]
print(Dolma)
print('\n')
Rozmarin = []
for x in range(10):
    Rozmarin.append(x)
print(Rozmarin)

women = ["Masha", "Nazgul", "Lera", "Regina"]
WOMEN = [x.upper() for x in women]
print(WOMEN)
WoMeN = [x if x!="Lera" else "Nikol" for x in women]
print(WoMeN)
women.sort()
print(women)

def cloose(n):
    return abs(20-n)

length = [14, 16, 16, 12, 9, 20]
#length.sort(reverse = True)
print(length)
length.sort(key = cloose)
print(length)

words = ["da", "Google", "Horse", "after", "beacon"]
words.sort(key = str.lower)
print(words)
words.reverse()
print(words)

#words2 = words.copy()
words2 = list(words)
print(words2)

# Sosiska = words + length
length.extend(words)
print(length)