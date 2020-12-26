k = int(input())
stk = []
for _ in range(k):
    num = int(input())

    if num != 0:
        stk.append(num)
    else:
        stk.pop()
print(sum(stk))