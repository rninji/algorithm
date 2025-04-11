import sys

# 입력
S = int(sys.stdin.readline())

# 풀이
i = 1
sum = 0
while(True):
    sum += i
    if sum >= S:
        break
    i+=1

# 출력
print(i if sum==S else i-1)