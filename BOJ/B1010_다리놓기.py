import math

# 입력
T = int(input())
NM = []
for _ in range(T):
  NM.append(list(map(int, input().split())))

# 풀이
for x in NM:
  print(math.comb(x[1], x[0]))