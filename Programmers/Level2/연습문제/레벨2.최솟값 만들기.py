def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    total = 0

    for a, b in zip(A, B):
        total += a * b

    return total