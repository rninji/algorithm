import sys
import heapq

# 입력
N = int(sys.stdin.readline())
assignment = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxday = max(assignment)[0]

# 풀이
answer = 0
heap = []
assignment.sort()
for day in range(maxday, 0, -1):
    for i in range(len(assignment)-1, -1, -1):
        if assignment[i][0] < day:
            break
        heapq.heappush(heap, -assignment.pop()[1])
    if heap:
        answer -= heapq.heappop(heap)
    
# 출력
print(answer)
    