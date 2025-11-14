from itertools import combinations

def solution(n, q, ans):
    res=[]

    arr=[i for i in range(1,n+1)]

    for comb in combinations(arr,5):
        now_correct=set(comb)
        ok=True
        for try_numbers,correct_num in zip(q,ans):
            now_try_numbers=set(try_numbers)
            if len(now_correct&now_try_numbers)==correct_num:
                continue
            else:
                ok=False
                break
        if ok:
            res.append(now_correct)

    answer=len(res)

    # print(res)

    return answer


# n=10
n=15
# q=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
q=[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
# ans=[2, 3, 4, 3, 3]
ans=[2, 1, 3, 0, 1]
print(solution(n,q,ans))