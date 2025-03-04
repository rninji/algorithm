# 입력
n,m = map(int, input().split())
num = list(map(int, input().split()))

# 풀이
max = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      now = num[i]+num[j]+num[k]
      if(now > max and now <= m):
        max = now

# 출력
print(max)