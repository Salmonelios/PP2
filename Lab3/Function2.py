import  itertools
def perm(s):
    return list(itertools.permutations(s))

def rev(s):
    d = ''
    words = s.split()
    for x in range(1, len(words)):
        d += words[-x]  + " "
    d += words[0]
    return d

def has_33(nums):
    for i in range(0, len(nums)):
        if nums[i]==3:
            if i-1>=0:
                if nums[i-1] == 3:
                    return True
            if i+1<=len(nums)-1:
                if nums[i+1]==3:
                    return True
    return False
        
print(perm("Ali"))
print(rev("We were here and you"))
print(has_33([3,1,3,3]))