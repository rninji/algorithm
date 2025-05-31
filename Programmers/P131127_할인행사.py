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

# 이하 딕셔너리 투포인터 사용 풀이
# def solution(want, number, discount):
#     answer = 0
#     wantDic = {}
#     newDic = {}
    
#     # 원하는 제품 딕셔너리 생성
#     for i in range(len(want)):
#         wantDic[want[i]] = number[i]
#         newDic[want[i]] = 0
#     # 10일치 품목 딕셔너리 설정
#     for w in discount[:10]:
#         if w in newDic:
#             newDic[w] += 1
#     if wantDic == newDic:
#         answer += 1     
        
#     # 2일차부터 확인
#     for i in range(1, len(discount) - 9):
#         if discount[i-1] in want:
#             newDic[discount[i-1]] -= 1
#         if discount[i+9] in want:
#             newDic[discount[i+9]] += 1
#         if wantDic == newDic:
#             answer += 1
    
#     return answer