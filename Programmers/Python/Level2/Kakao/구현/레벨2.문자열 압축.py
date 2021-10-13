def solution(s):
    n = len(s)
    answer = n

    # step 1부터 n//2까지
    for step in range(1, n // 2 + 1):
        result = ''
        cnt = 1
        prev = s[0:step]
        # step 부터 시작하여 n까지 step만큼의 범위씩 탐색
        for i in range(step, n, step):
            next = s[i:i + step]
            if prev == next:
                cnt += 1
            else:
                # cnt >= 2 인 경우에만 cnt 앞에 붙이고, 아니면 prev만
                result += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                # 다음 prev는 지금의 next
                prev = next
        # 마지막에 있는 ccc 가 연속된 것 등이나 a 하나만 있는 것을 붙여준다.
        result += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(result))

    return answer