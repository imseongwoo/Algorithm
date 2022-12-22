res = list(range(1,31))

for i in range(28):
    tmp = int(input())
    if tmp in res:
        res.remove(tmp)

res.sort()
for a in res:
    print(a)