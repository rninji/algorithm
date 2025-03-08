# 입력
n, k = map(int, input().split())
value = []
dp = [-1] * (k+1)
for _ in range(n):
  num = int(input())
  # k와 같은 값의 동전이 있다면 동전의 최소 개수는 1개
  if num == k:
    print(1)
    exit()
  elif num > k:
    continue
  value.append(num)
  dp[num] = 1

# 풀이
for i in range(1, k + 1): # i는 만들고싶은 가치
  if dp[i] == 1:
    continue
  minCnt = 10001
  for j in value: # j는 추가할 동전
    if i < j:
      continue
    if dp[i-j] > 0:
      minCnt = min(minCnt, dp[i-j]+1)
  if minCnt < 10001:
    dp[i] = minCnt

# 출력
print(dp[k])
