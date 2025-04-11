import sys
import heapq

# 입력
N = int(sys.stdin.readline())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))
    
# 풀이
if N == 1:
    print(0)
    exit(0)
    
sum = 0
while(len(cards) > 1):
    tmp = 0
    tmp += heapq.heappop(cards)
    tmp += heapq.heappop(cards)
    sum += tmp
    cards.append(tmp)
    
# 출력
print(sum)