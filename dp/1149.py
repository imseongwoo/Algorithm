n = int(input())
rgb = []
for i in range(1,n+1):
    rgb.append(list(map(int,input().split())))

for a in range(1,n):
    rgb[a][0] = min(rgb[a-1][1],rgb[a-1][2]) + rgb[a][0]
    rgb[a][1] = min(rgb[a-1][0],rgb[a-1][2]) + rgb[a][1]
    rgb[a][2] = min(rgb[a-1][0],rgb[a-1][1]) + rgb[a][2]

print(min(rgb[n-1]))