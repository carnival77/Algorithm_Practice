def solution(N, stages):
    answer = [0] * N

    frate = [0] * (N)
    total = len(stages)

    for i in range(1, N + 1):
        if total != 0:
            cnt = stages.count(i)
            frate[i - 1] = (i, cnt / total)
            total -= cnt
        else:
            frate[i - 1] = (i, 0)

    frate.sort(key=lambda x: (-x[1], x[0]))

    for i in range(N):
        answer[i] = frate[i][0]

    return answer