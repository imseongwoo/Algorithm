for t in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    result = 0
    for i in range(2, len(height) - 2):
        near = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        if near < height[i]:
            result += height[i] - near
    print("#" + str(t) + " " + str(result))
