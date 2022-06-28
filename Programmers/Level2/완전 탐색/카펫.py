def solution(brown, yellow):
    t = brown + yellow

    for x in range(t, 2, -1):
        if t % x == 0:
            y = t // x
            if yellow == (x - 2) * (y - 2):
                return [x, y]

    answer = []
    return answer