while True:
    arr = input()
    a = []
    if arr == '.':
        break
    for i in arr:
        if i == '(':
            a.append(i)
        elif i == '[':
            a.append(i)
        else:
            if i == ')':
                if '(' in a:
                    temp = a.pop()
                    a.append(temp)
                    if temp == '(':
                        a.pop()
                    else:
                        break
                else:
                    a.append(i)
                    break

            elif i ==']':
                if '[' in a:
                    temp = a.pop()
                    a.append(temp)
                    if temp == '[':
                        a.pop()
                    else:
                        break
                else:
                    a.append(i)
                    break

            else:
                continue
    if a:
        print('no')
    else:
        print('yes')

