def solution(progresses, speeds):
    answer = []
    while progresses:
        # 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 완성된 기능 배포
        cnt = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break
            cnt += 1
        if cnt:
            answer.append(cnt)
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]
    return answer