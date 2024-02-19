def square(n,m):
    for i in range(n, m+1):
        yield i **2
    
tim = square(3, 21)
for u in tim:
    print (u, end = " ")
    
print("\n")
    
def zero(n):
    for i in range(n+1):
        yield n-i
        
cnt = zero(32)

for u in cnt:
    print(u, end = " ")