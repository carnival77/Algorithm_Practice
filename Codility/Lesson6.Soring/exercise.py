# 문제:
# 정수 배열 A가 주어질 때, 서로 다른 값의 개수를 반환하라.
#
# 해법 O(n log n):
#
# 배열을 정렬하면 같은 값이 인접해서 모임.
#
# 인접한 값이 달라질 때마다 카운트 증가.

# 시간 복잡도: O(n log n) (정렬이 지배적)

def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for k in range(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result
