count,weight = map(int,input().split())

dp = [0] * (weight+1)

for i in range(count):
    w,v = map(int,input().split())
    for j in range(w,weight+1):
        dp[j] = max(dp[j],dp[j-w]+v)


print(dp[weight])

# 주어진 물건의 종류만큼 반복한다. 각 물건의 무게와 가치가 주어지면 그 무게부터 가방에 담을 수 있는 무게의 한계값
# 까지 내부 반복문을 사용하여 각 가방 무게에서 최대 가치가 될 수 있는 값을 dp 리스트에 저장한다.
# 최대값을 저장할 때 dp[j-w]+v 라고 작성한 이유는
# 주어진 물건을 사용한다고 가정하여 그 무게를 제외한 값의 dp의 최대값을 구한뒤 가치를 더해주는 작업을 반복하면 각 무게에서 최대의 가치를 구할 수 있기 때문이다
