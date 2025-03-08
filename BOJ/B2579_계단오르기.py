# 입력
n = int(input())
step = [0] * (n+1)
for i in range(1, n+1):
  step[i] = int(input())

# 풀이
dp = [0] * (n+1)
dp[0] = [0, 0]
dp[1] = [step[1], step[1]]

if (n>1):
  for i in range(2, n+1):
    # 전 계단 안 밟기
    no1 = max(dp[i-2][0], dp[i-2][1]) + step[i]
    # 전전 계단 안 밟기
    no2 = dp[i-1][0] + step[i]
  
    dp[i] = [no1, no2]

# 출력
print(max(dp[n][0], dp[n][1]))
              