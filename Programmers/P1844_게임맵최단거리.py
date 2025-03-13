di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    
    visit = [[10001 for i in range(m+1)] for j in range(n+1)]
    
    que = []
    que.append([1,1,1]) # 좌표 i, 좌표 j, 최소 이동 칸 수
    visit[1][1] = 1
    
    while(que):
        now = que.pop(0)
        
        # 사방탐색
        for k in range(4):
            ni = now[0] + di[k] # 다음 위치 i 
            nj = now[1] + dj[k] # 다음 위치 j
            ns = now[2] + 1 # 다음 가는데 걸리는 칸 수
            
            # 범위 외 스킵
            if ni < 1 or nj < 1 or ni > n or nj > m:
                continue
            # 더 빠르게 방문할 방법이 있거나 벽이면 스킵
            if visit[ni][nj]<=ns or maps[ni-1][nj-1] == 0:
                continue
            que.append([ni, nj, ns])
            visit[ni][nj] = ns
            
        answer =  -1 if visit[n][m]==10001 else visit[n][m]
    return answer