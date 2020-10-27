def solve(a:list) -> int:
    return print(sum(a))

n = int(input())
lis =[]
for _ in range(n):
    lis.append(int(input()))
solve(lis)