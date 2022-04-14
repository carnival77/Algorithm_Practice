from collections import Counter


def solution(clothes):
    ans = 1
    category = []

    for name, kind in clothes:
        category.append(kind)

    counter = Counter(category)

    result = list(counter.values())

    for i in result:
        ans *= (i + 1)

    ans -= 1

    return ans