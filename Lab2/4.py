list = ["Shura", "Egor Kreed", "Lazarev", "Kirkorov"]
for x in list:
    print(x)
    
print("\n")

for i in range(len(list)):
    print(list[i])
    
print("\n")
    
j = 0
while j<len(list):
    print(list[j])
    j+=1

print("\n")

[print(x) for x in list]