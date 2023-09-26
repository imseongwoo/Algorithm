arr = list(input())
stack = []
ref = []
operator_mapping = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': -1}

for a in arr:
    if a.isdigit():  # 숫자인 경우, 스택에 추가합니다
        stack.append(a)
    elif a == '(':  # 여는 괄호인 경우, 참조 스택에 추가합니다
        ref.append(a)
    elif a == ')':  # 닫는 괄호인 경우, 여는 괄호가 나올 때까지 참조 스택에서 연산자를 빼고 스택에 추가합니다
        while ref and ref[-1] != '(':
            stack.append(ref.pop())
        if ref and ref[-1] == '(':
            ref.pop()  # 여는 괄호를 꺼냅니다
    else:  # 연산자인 경우
        while ref and operator_mapping[ref[-1]] >= operator_mapping[a]:
            stack.append(ref.pop())
        ref.append(a)

while ref:  # 참조 스택에 남아 있는 연산자를 모두 뺍니다
    stack.append(ref.pop())

for a in stack:
    print(a,end='')