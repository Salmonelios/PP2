set = {"Okroshka", "compot", "draniki", "compot"}
print(set)
sset = {"blini", "sgushenka"}
set.update(sset)
print(set)
set.add("moloko")
print(set)
d = set.pop()
print(d)
print(set)
set.discard("kisel")
sett = {"Okrosthka", "compot", "dranniki", "compot"}
sett.intersection_update(set)
rrr = set.symmetric_difference(sett)
print(rrr)
print(sett)
if "Okroshka" in rrr:
    print("DA")