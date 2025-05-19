# # r1,c1   r2,c2
# 필요한 함수 : 영역 확인 함수, 미생물 영역 넓이 확인 함수
#
# [1]
# 1. n x n 크기 배열 생성 (초기값 0으로)
# 2. 직사각형 영역 숫자로 값 변경 (ex 1,2 ) 기존에 있던 값과 겹치면 새로 변경된 숫자로 덮어쓰기
# 3. bfs 돌면서 영역 개수 확인, 만약 영역 숫자 최대값보다 많다면 이전 무리의 미생물은 없어지므로 모두
# 0으로 변경
#
# [2]
# 4. nxn 새로운 배열 생성
# 5. 기존 배열에서 영역의 넓이 함수 실행하여 가장 넓은 무리 선택, 넓이가 같다면 먼저 투입된(숫자가 작은)
# 6. x좌표, y좌표 최소값 위치로 r1,c1 이동 차이만큼 r2,c2도 이동, 다른 미생물 영역과 겹치거나 nxn을
# 벗어나면 그냥 사라짐
#
# [3]
# 7. 각 미생물 영역 넓이끼리 곱한 후 결과 배열에 저장

from collections import deque
from collections import defaultdict

def calculate_score_with_bfs(arr, N):
    visited = [[False]*N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    component_sizes = defaultdict(int)  # 각 미생물 ID의 전체 넓이
    adjacent_pairs = set()              # 인접한 미생물 ID 쌍

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0 and not visited[r][c]:
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                curr_id = arr[r][c]
                size = 1  # 이 연결 컴포넌트의 넓이

                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and arr[nx][ny] == curr_id:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                size += 1
                            elif arr[nx][ny] != 0 and arr[nx][ny] != curr_id:
                                a, b = sorted((curr_id, arr[nx][ny]))
                                adjacent_pairs.add((a, b))

                component_sizes[curr_id] += size

    # 인접한 쌍의 넓이 곱 점수 계산
    score = 0
    for a, b in adjacent_pairs:
        score += component_sizes[a] * component_sizes[b]

    return score


def move_microbes_corrected(arr, N):
    from collections import defaultdict

    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    microbe_positions = defaultdict(list)

    # 미생물별 좌표 모음
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                microbe_positions[arr[r][c]].append((r, c))

    # (넓이 큰 순, ID 큰 순) 정렬
    microbe_info = []
    for micro_id, cells in microbe_positions.items():
        rows = [r for r, c in cells]
        cols = [c for r, c in cells]
        min_r, max_r = min(rows), max(rows)
        min_c, max_c = min(cols), max(cols)
        h = max_r - min_r + 1
        w = max_c - min_c + 1

        # 모양 저장
        shape = [[0] * w for _ in range(h)]
        for r, c in cells:
            shape[r - min_r][c - min_c] = micro_id

        microbe_info.append((-len(cells), -micro_id, micro_id, shape, h, w))

    microbe_info.sort()

    # 좌하단부터 빈 곳 탐색하며 배치
    for _, _, micro_id, shape, h, w in microbe_info:
        placed = False
        for sr in reversed(range(N - h + 1)):  # 아래 → 위
            for sc in range(N - w + 1):        # 왼쪽 → 오른쪽
                can_place = True
                for i in range(h):
                    for j in range(w):
                        if shape[i][j] == 0:
                            continue
                        if new_arr[sr + i][sc + j] != 0:
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    for i in range(h):
                        for j in range(w):
                            if shape[i][j] != 0:
                                new_arr[sr + i][sc + j] = micro_id
                    placed = True
                    break
            if placed:
                break

    return new_arr






def count_regions(arr, N):
    visited = [[False]*N for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dict_cnt = {}

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0 and not visited[r][c]:
                if arr[r][c] not in dict_cnt:
                    dict_cnt[arr[r][c]] = 0
                dict_cnt[arr[r][c]] += 1

                q = deque()
                q.append((r,c))
                visited[r][c] = True

                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and arr[nx][ny] == arr[r][c]:
                                visited[nx][ny] = True
                                q.append((nx,ny))
    for key in dict_cnt.keys():
        if dict_cnt[key] >= 2:
            for r in range(N):
                for c in range(N):
                    if arr[r][c] == key:
                        arr[r][c] = 0


N, Q = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    c1, c2 = N - c2, N - c1  # 반전

    for row in range(c1, c2):
        for col in range(r1, r2):
            arr[row][col] = i + 1
    count_regions(arr, N)
    arr = move_microbes_corrected(arr,N)
    score = calculate_score_with_bfs(arr, N)
    print("점수:", score)
    # 확인용 출력
    for row in arr:
        print(" ".join(map(str, row)))




