# 탑다운
n,k = map(int, input().split())

d = [0] * 100000000


def f(n, k):
    if k == 0:
        return 1
    if d[k] != 0:
        return d[k]
    d[k] = f(n, k - 1) * n

    return d[k]


a = f(n, k)
print(a)

#바텀업 방식

# n, k = map(int, input().split())
#
# d = [0] * 100000000
# d[0] = 1
#
# for i in range(1, k + 1):
#     d[i] = d[i - 1] * n
#
# result = d[k] % 1000000007
# print(result)

