# 각각의 추를 저울의 오른쪽에 놓을지 왼쪽에 놓을지 아예 놓지 않을지에 대한 경우를 모두 탐색하여 set 자료형
# 에 넣고 처리한다.
def dfs(l,sum):
    if l==k+1:
        return

    else:
        a.add(sum)      # 현재 무게를 집합에 넣어줌
        dfs(l+1,sum + arr[l])   # 무게를 더하는 경우
        dfs(l+1,sum - arr[l])   # 무게를 빼는 경우
        dfs(l+1,sum)            # 무게를 올려놓지 않는 경우


count = 0       # 측정 불가능한 가지수 측정 변수
a = set()
k = int(input())
arr = list(map(int,input().split()))
arr.append(0)
dfs(0,0)
for num in range(sum(arr)):
    if num not in a:
        count += 1

print(count)


