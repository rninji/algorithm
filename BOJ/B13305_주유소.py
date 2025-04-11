import sys

# 입력
N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

# 풀이
answer = 0
min_price = 1e9
for i in range(len(price)-1):
    if min_price > price[i]:
        min_price = price[i]
    answer += road[i] * min_price

# 출력
print(answer)