import sys

# 입력
N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))

# 풀이
stack = [[0, top[0]]] # 탑 번호, 높이
print(0, end=' ') # 첫번째 탑은 수신 불가
if N <= 1:
    exit(0)

for i in range(1, len(top)):
    while stack:
        left = stack[len(stack)-1]
        if left[1] >= top[i]:
            print(left[0]+1, end=' ')
            break
        else:
            stack.pop()

    if not stack:
        print(0, end=' ')
    stack.append([i, top[i]])