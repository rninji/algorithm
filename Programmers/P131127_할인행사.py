def solution(want, number, discount):
    answer = 0
    wantList = []
    for i in range(len(want)):
        for j in range(number[i]):
            wantList.append(want[i])
    wantList.sort()
    
    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        tmp.sort()
        if tmp == wantList:
            answer+=1
            
    return answer