def find(x, connection):
    if x == connection[x]: return x
    else: return find(connection[x], connection)

def union(x, y, connection):
    x = find(x, connection)
    y = find(y, connection)
    if x<y: connection[y] = x
    else: connection[x] = y
    return connection

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:-x[2])
    connection = [i for i in range(n)]
    
    while(costs):
        now = costs.pop()
        if find(now[0], connection)==find(now[1], connection): # 이미 이어진 섬인 경우 스킵
            continue
        connection = union(now[0], now[1], connection) # 섬 연결
        answer += now[2]
    
    return answer