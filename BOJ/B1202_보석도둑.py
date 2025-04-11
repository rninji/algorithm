import sys
import heapq

# 입력
N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

# 풀이
jewels.sort(reverse=True)
bags.sort()
heap = []
answer = 0

for bag in bags: # 작은 가방부터
    for i in range(len(jewels)-1, -1, -1): # 무게 적은 보석부터 
        if jewels[i][0] > bag:
            break
        heapq.heappush(heap, -jewels[i][1]) # 현재 가방에 넣을 수 있다면 가격 삽입
        jewels.pop()
    if heap:
        answer+= -heapq.heappop(heap) # 넣을 수 있는 보석 중 가장 비싼 보석
    
# 출력
print(answer)