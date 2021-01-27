arr = list(input())
stk = []
ref = []
for a in arr:
    if a.isdigit():
        stk.append(a)
    else:
        if a == '+':
            b = int(stk.pop())
            a = int(stk.pop())
            stk.append(a+b)
        elif a == '-':
            b = int(stk.pop())
            a = int(stk.pop())
            stk.append(a - b)
        elif a == '*':
            b = int(stk.pop())
            a = int(stk.pop())
            stk.append(a * b)
        elif a == '/':
            b = int(stk.pop())
            a = int(stk.pop())
            stk.append(a / b)
        else:
            continue
print(sum(stk))
