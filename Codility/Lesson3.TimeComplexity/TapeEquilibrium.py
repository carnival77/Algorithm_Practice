import sys

def solution(A):
    total = sum(A)
    left = 0
    ans = sys.maxsize
    for i in range(len(A) - 1):   # P는 1..N-1
        left += A[i]
        ans = min(ans, abs(total - 2 * left))
    return ans
