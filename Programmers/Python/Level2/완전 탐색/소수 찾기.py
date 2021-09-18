from itertools import permutations
import math

def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    arr = list(numbers)

    answer = set()

    for i in range(1,len(arr)+1):
        tgs = list(permutations(arr, i))
        for j in tgs:
            j = int("".join(list(j)))
            if j >= 2:
                if check(j):
                    answer.add(j)

    return len(answer)


# 모범 답안
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)