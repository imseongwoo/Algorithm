n = int(input())

d = []
d.append(0)
d.append(1)
d.append(2)

for a in range(3,46):
    temp = d[a-2] + d[a-1]
    d.append(temp)

print(d[n])
