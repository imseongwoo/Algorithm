must = list(input())
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())
for a in arr:
    count = 0
    ref = []

    a = list(a)
    num = len(a)
    for x in a:
        if x in must:
            if not x in ref:
                ref.append(x)
        else:
            continue
    if any(ref[y] != must[y] for y in range(len(ref))):
        print('NO')
    else:
        print('YES')


