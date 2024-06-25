for t in range(10):
    count = int(input())
    height = list(map(int, input().split()))

    for i in range(count):
        height.sort()
        height[-1] -= 1
        height[0] += 1
    print(f"#{t+1} {max(height) - min(height)}")
