def solution(players, m, k):
    answer = 0
    server = [25]
    for i in range(len(players)):
        # 서버 체크
        for j in range(len(server)-1, -1, -1):
            if server[j] == i:
                server.pop(j)
            
        # 이용자 수 확인 후 증설
        nowplay = players[i]
        if nowplay < len(server) * m:
            continue
        new = nowplay//m + 1 - len(server)
        answer += new
        for _ in range(new):
            server.append(i+k)
    return answer
