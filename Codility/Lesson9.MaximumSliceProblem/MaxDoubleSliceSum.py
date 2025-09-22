# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    a = A
    n = len(a)

    max_slice = 0
    max_ending = [0] * n
    max_start = [0] * n

    for i in range(1, n - 1):
        max_ending[i] = max(max_ending[i - 1] + a[i], 0)

    for i in range(n - 2, 0, -1):
        max_start[i] = max(max_start[i + 1] + a[i], 0)

    for y in range(1, n - 1):
        max_slice = max(max_slice, max_ending[y - 1] + max_start[y + 1])

    return max_slice