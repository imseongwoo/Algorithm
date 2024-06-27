T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m][m + 1] = arr[m + 1][m] = 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d     # 입력뱓은 좌표에 돌 놓기

        # 8방향 탐색
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)):
            r = []
            for mul in range(1, N): # 뻗어나가는 거리
                ni, nj = si + di * mul, sj + dj * mul
                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:    # 빈칸이면 탐색 중단
                        break
                    elif arr[ni][nj] == d:  # 같은돌이면 후보들 뒤집기
                        while r:
                            ti, tj = r.pop()
                            arr[ti][tj] = d
                        break
                    else:   # 다른돌이면 뒤집을 후보에 추가
                        r.append((ni, nj))
                else:
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{test_case} {bcnt} {wcnt}')