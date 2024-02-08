def histogram(listt):
    for i in listt:
        for x in range(0, i):
            print("*", end = "")
        print(" ")
histogram([1, 5, 4, 12])