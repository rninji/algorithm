def solution(friends, gifts):
    answer = 0
    record = [[0] * len(friends) for _ in range(len(friends))]
    gfp = {} # 선물지수
    nmon = {} # 다음달 받을 선물 개수
    for f in friends:
        gfp[f] = 0
        nmon[f] = 0
        
    #주고받은 선물 및 선물 지수 측정
    for g in gifts:
        give, get = g.split()
        gfp[give] += 1
        gfp[get] -= 1
        record[friends.index(give)][friends.index(get)] += 1
    
    #다음달 예측
    for i in range(len(friends)):
        for j in range(i, len(friends)):
            # 주고받은 기록이 있는 경우
            if record[i][j] > record[j][i]:
                nmon[friends[i]] += 1
            elif record[i][j] < record[j][i]:
                nmon[friends[j]] += 1
            # 주고받은 기록이 없거나 수가 같은 경우 - 선물 지수 측정
            else:
                if gfp[friends[i]]==gfp[friends[j]]: 
                    continue
                elif gfp[friends[i]]>gfp[friends[j]]:
                    nmon[friends[i]] += 1
                else:
                    nmon[friends[j]] += 1
    return max(nmon.values())
