def solution(name):
    answer = 0

    l = len(name)

    min_move = l - 1

    for i in range(l):
        c = ord(name[i])
        move = min(c - ord('A'), ord('Z') - c + 1)
        answer += move

        nextIdx = i + 1
        while nextIdx < l and name[nextIdx] == 'A':
            nextIdx += 1
        min_move = min(min_move, i * 2 + l - nextIdx)

    answer += min_move

    return answer