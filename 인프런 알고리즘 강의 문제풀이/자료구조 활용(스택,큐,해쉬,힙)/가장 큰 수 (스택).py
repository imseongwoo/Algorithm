# 다시 풀어보기!!!!!!!!!!!!!!!!!!!!!!!
n,m = map(int,input().split())
ref = []
while n>0:
    ref.append(n%10)
    n=n//10
ref.reverse()
stack = []
stack.append(ref.pop(0))
for x in ref:
    while stack and m>0 and stack[-1] <x:
        stack.pop()
        m-=1
    if not stack or m<=0 or stack[-1] >= x:
        stack.append(x)

if m!=0:
    stack = stack[:-m]
print(stack)

