def solution(name):
    alpha = 0
    move = len(name)-1 # 오른쪽으로만 움직이는 경우
    startA = -1

    for i in range(len(name)):
        n = name[i]
        alpha += min(ord(n)-65, 91-ord(n))

        if n!= 'A':
            startA = -1
        else:
            if startA==-1: startA=i # startA ~ i는 'A'
            right = 0 if startA==0 else startA-1
            left = len(name)-i-1
            move = min(move, right+left+min(right,left))

    return alpha + move