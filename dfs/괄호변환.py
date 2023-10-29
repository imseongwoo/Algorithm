def check(string):
    stack = []

    for a in string:
        if a=='(':
            stack.append(a)
        elif a==')':
            if stack:
                stack.pop()
            else:
                return False
    return True

def dfs(w):
    close = 0
    if not w:
        return w
    else:
        for i in range(len(w)):
            if w[i] == '(': close += 1
            else: close -= 1

            if close==0:
                if check(w[:i+1]):
                    return ''.join([w[:i+1], dfs(w[i+1:])])
                else:
                    v = ['(',dfs(w[i+1:]),')']
                    for a in range(1,i):
                        if w[a]=='(':
                            v.append(')')
                        else: v.append('(')
                    return ''.join(v)

def solution(p):
    return dfs(p)

print(solution("(()())()"))

