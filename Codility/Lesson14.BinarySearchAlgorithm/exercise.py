# 문제:
#
# 배열 A가 주어짐 (0 또는 1). 1은 구멍(holes).
#
# 길이가 같은 판자 k개가 있음.
#
# 모든 구멍을 덮을 수 있는 판자의 최소 길이를 구하라.
#
# 아이디어:
#
# 길이 x가 충분하다면 x+1, x+2, …도 충분.
#
# 길이 x가 부족하다면 x-1, x-2, …도 부족.
# → 즉, “충분/부족”이 경계 지점을 기준으로 단조(monotonic).
# → 이 성질을 이용해 이진 탐색.

# check(A, mid) → 길이가 mid인 판자로 몇 개나 필요한지 계산.
#
# <= k면 가능, 아니면 불가능.
#
# 전체 시간복잡도: O(n log n)

def boards(A, k):
    n = len(A)
    beg = 1
    end = n
    result = -1
    while beg <= end:
        mid = (beg + end) // 2
        if check(A, mid) <= k:
            result = mid
            end = mid - 1
        else:
            beg = mid + 1
    return result

def check(A, k):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1  # 현재 구멍 i를 덮는 판자 범위의 끝
    return boards
