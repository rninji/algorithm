# 입력
n = int(input())
num = []
for i in range(n):
  num.append(int(input()))

# 풀이
num.sort()

# 출력
for i in num:
  print(i)