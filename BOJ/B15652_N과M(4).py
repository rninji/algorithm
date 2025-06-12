# 입력
N, M = map(int, input().split())


def func(num, save, arr):
    # 출력
    if len(save) == M:
        for s in save:
            print(s, end=' ')
        print()
        return;
    # 백트래킹
    for i in range(len(arr)):
        save.append(arr[i])
        func(arr[i] , save, arr[i:])
        save.pop()

# 초기 배열
arr = [i for i in range(1, N+1)]
for i in range(1, N+1):
    func(i, [i], arr[i-1:])