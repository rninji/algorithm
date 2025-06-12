import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
people = [[False, set()] for _ in range(N + 1)]
know = list(map(int, sys.stdin.readline().split()))
know_cnt = know.pop(0)

party = []
for i in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    line.pop(0)
    party.append(line)
    # 함께 하는 파티원 기록
    for j in line:
        people[j][1].update(line)
        people[j][1].remove(j)

# 진실을 아는 경우 함께 파티하는 사람들도 진실을 알게 함
def knowing(person):
    if people[person][0]:
        return
    people[person][0] = True
    for next in people[person][1]:
        knowing(next)

for k in know:
    knowing(k)
        
# 파티 개수 확인
answer = 0
for pt in party:
    can = True
    for ps in pt:
        if people[ps][0]:
            can = False
            break;
    if can:
        answer += 1

# 출력
print(answer)
