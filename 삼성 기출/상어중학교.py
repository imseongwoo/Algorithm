N, M = map(int, input().split())
EMPTY=M+1
# 4방향을 -1로 둘러쌈 (범위체크 필요없음)
arr = [[-1]*(N+2)]+[[-1]+list(map(int, input().split()))+[-1] for _ in range(N)]+[[-1]*(N+2)]

from collections import deque
def bfs():
    # 미방문 일반블럭에서 BFS 확산(가장 큰 크기=> .. )
    v = [[0]*(N+2) for _ in range(N+2)]
    mx_group = set()
    mx_rcnt=0
    for si in range(1,N+1):
        for sj in range(1,N+1):
            if v[si][sj]==0 and 0<arr[si][sj]<=M:   # 미방문 일반블럭
                q = deque()
                group=set()

                q.append((si,sj))
                group.add((si,sj))
                v[si][sj]=1
                color=arr[si][sj]
                r_cnt=0

                while q:
                    ci,cj=q.popleft()
                    # 네방향, 미방문(일반블럭 또는 무지개),같은색깔 또는 무지개블럭
                    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni,nj=ci+di,cj+dj
                        if v[ni][nj]==0 and (ni,nj) not in group and (arr[ni][nj]==color or arr[ni][nj]==0):
                            q.append((ni,nj))
                            group.add((ni,nj))
                            if arr[ni][nj]==0:  # 무지개인경우
                                r_cnt+=1
                            else:               # 일반블록
                                v[ni][nj]=1

                # 그룹개수 > 같으면 rcnt 큰값 > 행 > 열
                if len(mx_group)<len(group) or (len(mx_group)==len(group) and mx_rcnt<=r_cnt):
                    mx_group, mx_rcnt = group, r_cnt
    return mx_group

def gravity():
    for si in range(1,N):
        for sj in range(1,N+1): # 전체를 순회
            ci,cj=si,sj
            # 내위치 블럭(일반,무지개)이고, 아래칸이 빈칸이면 교환(위로 반복)
            while 0<=arr[ci][cj]<=M and arr[ci+1][cj]==EMPTY:
                arr[ci][cj],arr[ci+1][cj]=arr[ci+1][cj],arr[ci][cj]
                ci-=1

ans = 0
while True:                  # 선택한 그룹 개수가 2개 미만이면 종료
    del_group = bfs()       # [1] 미방문 일반블럭 기준으로 블럭그룹 찾기
    if len(del_group)<2:
        break

    ans += len(del_group)**2
    for ti,tj in del_group: # [2] 선택한 블럭 삭제(점수에 추가)
        arr[ti][tj]=EMPTY

    gravity()               # [3] 중력

    # [4] 반시계방향 90도 회전
    arr=list(map(list,zip(*arr)))[::-1]

    gravity()               # [5] 중력
print(ans)