from collections import Counter
from functools import reduce


def solution(clothes):
    # answer = 1

    #     category=[]
    #     for i in clothes:
    #         category.append(i[1])

    #     cnt = Counter(category)

    #     result=list(cnt.values())

    #     for i in result:
    #         answer *= (i+1)

    #     answer-=1

    cnt = Counter([kind for cloth, kind in clothes])

    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1

    return answer