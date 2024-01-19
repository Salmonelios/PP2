import random

print(random.randrange(1, 11))
print(float(random.randrange(1, 11)))

a = """In garden is acacia bloom
I walk without hiding a smile
Today I have exam"""
print(a)
print(a[5])

# for i in a:
#    print(i)

print(len(a))

if "garden" in a:
    print("yes")

print("Is" not in a)

print(a[:10])
print(a[5:])
print(a[-5:-2])