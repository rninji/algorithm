# 입력
n = int(input())

# 풀이
num = 1
cnt = 0
while(True):
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1
    
# 출력
print(num)
