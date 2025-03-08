# 입력
N = int(input())
cost = []
for i in range(N):
  cost.append(list(map(int, input().split())))

# 풀이
dp = [0] * N
dp[0] = [cost[0][0], cost[0][1], cost[0][2]]
for i in range(1, N):
  costR = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
  costG = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
  costB = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
  dp[i] = [costR, costG, costB]

# 출력
print(min(dp[N-1]))