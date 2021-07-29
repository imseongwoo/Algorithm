# 다시 풀기
arr = list(input())
stk =[]
ref = []
for a in arr:
    if a.isdigit():
        stk.append(a)
        # if '+' in ref and '*' in ref and len(ref)==2:
        #     stk.append(ref.pop())
        # elif '-' in ref and '*' in ref and len(ref)==2:
        #     stk.append(ref.pop())
        # elif '+' in ref and '/' in ref and len(ref)==2:
        #     stk.append(ref.pop())
        # elif '-' in ref and '/' in ref and len(ref) == 2:
        #     stk.append(ref.pop())

    else:
        if a == '(':
            ref.append(a)
            continue
        elif a == ')':
            while ref:
                stk.append(ref.pop())

        else:
            ref.append(a)

if ref:
    while ref:
        stk.append(ref.pop())
stk.remove('(')
for a in stk:
    print(a,end='')
