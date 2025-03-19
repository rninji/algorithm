import sys
# 입력
N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

# 풀이
def findTeam(cnt, n):
    global answer
    if cnt == N//2: # 멤버 선택 완료, 능력치 계산
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    start += S[i][j]
                elif not visit[i] and not visit[j]:
                    link += S[i][j]
        answer = min(answer, abs(start-link))
        return
    else: # 다음 노드 선택
        for i in range(n+1, N):
            visit[i] = True
            findTeam(cnt+1, i)
            visit[i] = False

answer = float('inf')
visit = [False] * N
visit[0] = True
findTeam(1,0)

# 출력
print(answer)