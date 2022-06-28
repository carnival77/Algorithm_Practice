def solution(n, a, b):
    answer = 0

    left = min(a, b)
    right = max(a, b)

    while True:
        dif = right-left
        if left % 2 != 0 and dif==1:
            break

        left = (left + 1) // 2
        right = (right + 1) // 2

        answer += 1

    return answer

print(solution(8,4,7))