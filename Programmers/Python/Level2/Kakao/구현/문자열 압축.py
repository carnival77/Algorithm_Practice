def solution(s):
    n = len(s)
    answer = n

    for step in range(1, n // 2 + 1):
        result = ''
        cnt = 1
        prev = s[0:step]
        for i in range(step, n, step):
            next = s[i:i + step]
            if prev == next:
                cnt += 1
            else:
                result += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = next
        result += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(result))

    return answer