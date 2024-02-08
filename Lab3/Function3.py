def spy_game(nums):
    cnt = 0
    for i in nums:
        if i==0 and cnt==0:
            cnt += 1
        elif i==0 and cnt==1:
            cnt += 1
        elif i==7 and cnt==2:
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False
    
def volume(r):
    return 4/3*3.14*r**3

def unoque(listt):
    new = []
    for i in listt:
        if i not in new:
            new.append(i)
    return new
def poli(s):
    d = len(s)-1
    for i in s:
        if i != s[d]:
            return False
        d -= 1
    return True
        
    
print(spy_game([1, 2, 3, 4,0, 7, 7, 0, 4, 7, 5]))
print(volume(5))
print(unoque([1, 2, 3, 4, 4, 3, 2, 1, 1, 1, 1]))
print(poli("madam"))
