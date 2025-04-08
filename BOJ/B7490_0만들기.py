# 입력
T = int(input())

# 풀이
def make(case, num):
    new_case = []
    insert = [' ','+', '-']
    for c in case:
        for i in insert:
            new_case.append(c+str(num)+i)
    return new_case

def cal(case):
    answer = 0
    tmp = 0
    add = True
    for i in range(len(case)):
        if case[i].isdigit():
            tmp += int(case[i])
            if i == len(case)-1:
                if add: 
                    answer += tmp
                else:
                    answer -= tmp
        elif case[i] == ' ':
            tmp = tmp*10
        else:
            if add: 
                answer += tmp
            else:
                answer -= tmp
            tmp = 0
            if case[i] == '+':
                add = True
            elif case[i] == '-' :
                add = False
    return answer

for _ in range(T):
    N = int(input())
    case = ['']
    
    # 수식 생성
    for i in range(1, N):
        case = make(case, i)
    for i in range(len(case)):
        case[i] = case[i]+str(N)

    # 수식 계산
    for c in case:
        answer = cal(c)
        if answer == 0:
            print(c)
    print('')
