# n = int(input())
# timelist = []
#
# count = 1
# for i in range(n):
#     timelist.append(list(map(int,input().split())))
#
#
# timelist = sorted(timelist,key=lambda x:(x[1],x[0])) # 끝나는 시간을 기준으로 정렬하고 시작시간 기준으로도 정렬
# minnum = timelist[0][1]
#
# for i in range(n-1):
#     if timelist[i+1][0] >= minnum:
#         minnum = timelist[i+1][1]
#         count += 1
#
# print(count)
n = int(input())
timelist = []

count = 1
for i in range(n):
    timelist.append(list(map(int,input().split())))


timelist = sorted(timelist,key=lambda x:(x[1],x[0]))
minnum = timelist[0][1]

for i in range(1,n):                # **중요** 시작하는 시간이 끝나는 시간과 같은 경우를 고려해야함
    if timelist[i][0] >= minnum:
        minnum = timelist[i][1]
        count += 1

print(count)