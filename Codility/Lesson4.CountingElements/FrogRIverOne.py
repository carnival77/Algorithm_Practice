def solution(X, A):

    seen = [False] * (X + 1)
    remain=X

    for t, pos in enumerate(A):
        if not seen[pos]:
            seen[pos]=True
            remain-=1
            if remain==0:
                return t

    return -1