# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import combinations

def solution(E):

    ans=0
    a=[[] for _ in range(10)]

    for emp_num,days in enumerate(E):
        # days=list(days)
        for day in days:
            day_num=int(day)
            a[day_num].append(emp_num)

    for r in [1,2]:
        for comb in combinations(a,2):
            tmp=set()
            for group in comb:
                tmp.update(group)
            ans=max(ans,len(tmp))

    return ans

# E=["039","4","14","32","34","7"]
E=["801234567","180234567","0","189234567","891234567","98","9"]
print(solution(E))