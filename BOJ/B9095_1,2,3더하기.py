# 입력
T = int(input())
TC = []
for _ in range(T):
  TC.append(int(input()))

# 풀이
max = max(TC)
dp = [0] * (max + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max+1):
  for j in range(1, 4):
    dp[i]+=dp[i-j]

# 출력
for i in TC:
  print(dp[i])