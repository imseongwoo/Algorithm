arr = list(input())
stack = []
cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')' and arr[i-1] != '(':
        stack.pop()
        cnt += 1
    elif arr[i] == ')' and stack[-1] == '(':
        stack.pop()
        cnt += len(stack)

print(cnt)