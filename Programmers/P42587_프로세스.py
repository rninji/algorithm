def solution(priorities, location):
    que = [i for i in range(len(priorities))]
    time = 0
    while priorities:
        fp = priorities.pop(0)
        fq = que.pop(0)
        is_back = False
        for p in priorities:
            if p > fp:
                priorities.append(fp)
                que.append(fq)
                is_back = True
                break
        if not is_back:
            time += 1
            if fq == location:
                return time
    return 0