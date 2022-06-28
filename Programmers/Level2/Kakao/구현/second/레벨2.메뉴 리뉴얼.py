from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for goal in course:
        all=[]
        for order in orders:
            for c in combinations(sorted(order),goal):
                all.append(c)
        ct=Counter(all)

        if len(all)==0:
            break

        most_ordered_cnt=ct.most_common(n=1)[0][1]

        for key,value in ct.items():
            if value==most_ordered_cnt and value!=1:
                answer.append(''.join(list(key)))

    return sorted(answer)

# orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course=	[2,3,4]
# orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course=[2,3,5]
orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]
print(solution(orders,course))