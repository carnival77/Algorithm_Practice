def solution(s):
    answer = 0

    input_str = s

    length = len(input_str)

    count = 0
    comp = ""
    answer = length

    for unit in range(1, length // 2 + 1):
        comp = ""
        prev = input_str[0:unit]
        count = 1
        for i in range(unit, length, unit):
            next = input_str[i:i + unit]
            if prev == next:
                count += 1
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = input_str[i:i + unit]
                count = 1
        comp += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(comp))

    return answer