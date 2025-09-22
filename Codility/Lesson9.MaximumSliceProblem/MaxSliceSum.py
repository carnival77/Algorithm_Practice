"""
아이디어: Kadane's Algorithm (빈 구간 불허)
시간: O(N), 공간: O(1)
"""

def solution(A):
    a = A
    max_slice = max_ending = a[0]

    for x in a[1:]:
        max_ending = max(x, max_ending + x)
        max_slice = max(max_ending, max_slice)
    return max_slice