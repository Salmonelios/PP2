import math

lst = [1, 2, 3, 4, 5]
multi = math.prod(lst)
print(multi)

sttr = input()
low = 0
upp = 0

for i in sttr:
    if i.isupper():
        upp += 1
    else:
        low += 1
        
print(f"Number of lower case is {low}")
print(f"Number of upper case is {upp}")

poli = input()
rpoli = ''.join(reversed(poli))
if poli == rpoli:
    print("Is polindrome")
else:
    print("Is not polindrome")
