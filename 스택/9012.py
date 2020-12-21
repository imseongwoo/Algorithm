

n = int(input())

for _ in range(n):
    stk = list(input())

    while stk:
        if stk[0] == ')':
            print('NO')
            break
        else:
            if ')' in stk:
                stk.remove('(')
                stk.remove(')')
            else:
                print('NO')
                break

    if not stk:
        print('YES')


