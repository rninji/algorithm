def findNum(string):
    answer = 0
    digit = 0
    for i in range(len(string)-1, -1, -1):
        num = ord(string[i])-96
        answer+=num * 26**digit
        digit+=1
    return answer

def findStr(n):
    string = ''
    while(True):
        string = chr((n-1)%26+97)+string
        if n//26 == 0:
            break
        n =(n-1)//26
    return string

def solution(n, bans):
    bansToNum = []
    for b in bans:
        bansToNum.append(findNum(b))
    bansToNum.sort()
    for b in bansToNum:
        if b <= n:
            n+=1
    return findStr(n)
