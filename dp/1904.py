import sys
n = int(sys.stdin.readline())

d = [-1] * 1000001
d[0] = 0
d[1] = 1
d[2] = 2

for i in range(3,n+1):
    d[i] = (d[i-1]  + d[i-2]) % 15746

print(d[n])