def even(s):
    for x in range(s+1):
        if x%2 == 0:
            yield x
    
n = int(input())    
asn = list(even(n))
print(", ".join(map(str, asn)))