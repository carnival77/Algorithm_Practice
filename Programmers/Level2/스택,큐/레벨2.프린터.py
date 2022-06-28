from collections import deque


def solution(priorities, location):
    answer = 0

    a = deque()

    for inx, ele in enumerate(priorities):
        a.append((ele, inx))

    while a:
        tmp = a.popleft()
        if len(a) > 0:
            if tmp[0] < max(a)[0]:
                a.append(tmp)
            else:
                answer += 1
                if tmp[1] == location:
                    return answer
        else:
            answer += 1
            if tmp[1] == location:
                return answer

    return answer