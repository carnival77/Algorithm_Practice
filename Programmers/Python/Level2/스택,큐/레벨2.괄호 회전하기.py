from collections import deque

def solution(s):
    answer = 0
    left = ["(", "{", "["]

    n = len(s)

    s2 = deque(s)

    def check(s):
        stack = []
        for y in s:
            if y in left:
                stack.append(y)
            else:
                if not stack:
                    return False
                else:
                    tg = stack.pop()
                    if y == ")" and tg != "(":
                        return False
                    elif tg != "{" and y == "}":
                        return False
                    elif tg != "[" and y == "]":
                        return False

        return len(stack) == 0

    for x in range(n):
        s2.rotate(-1)

        if check(s2):
            answer += 1

    return answer