# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    arr = [0] * N

    max_val = 0
    adjust_val = 0
    for x in A:
        if 1 <= x <= N:
            if arr[x - 1] < adjust_val:
                arr[x - 1] = adjust_val + 1
            else:
                arr[x - 1] += 1
            max_val = max(arr[x - 1], max_val)
        elif x == N + 1:
            adjust_val = max_val

    for i in range(len(arr)):
        if arr[i] < adjust_val:
            arr[i] = adjust_val

    return arr