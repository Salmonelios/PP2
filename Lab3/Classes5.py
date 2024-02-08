def prime(a):
    if a > 2:
        for n in range(2, a):
            if a%n == 0:
                return False
    else:
        return True
    return True


listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 21, 23]
print(list(filter(lambda x:prime(x), listt)))