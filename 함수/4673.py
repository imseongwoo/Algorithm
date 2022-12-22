def selfnumer(val):
    S = list(map(int, str(val)))

    return val + sum(S)

checker = []

for i in range(10000):
    checker.append(selfnumer(i))

    if i in checker:
        pass
    else:
        print(i)


