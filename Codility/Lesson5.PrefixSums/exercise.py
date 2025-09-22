# 길을 따라 n개의 위치에 버섯이 자라고 있고, 각 위치마다 배열 A에 버섯 수가 주어진다.
#
# 채집자는 위치 k에서 출발하고, 최대 m번 이동할 수 있다.
#
# 한 번 이동은 인접한 위치로 이동하는 것.
#
# 채집자는 방문한 위치의 버섯을 모두 채집한다.
#
# 목표: 최대 몇 개의 버섯을 채집할 수 있는가?

# 예시:
#
# A = [2, 3, 7, 5, 1, 3, 9]
# 인덱스 = 0  1  2  3  4  5  6
#
#
# 시작 위치 k = 4, 이동 횟수 m = 6
#
# 이동 경로 예: 4→3→2→3→4→5→6
#
# 채집 버섯: 1 + 5 + 7 + 3 + 9 = 25 → 최대 값

# O(n + m) 해법 (접두사 합 활용)
#
# 접두사 합을 사용하면 훨씬 빨라집니다.
#
# p번을 왼쪽으로 이동하면, 오른쪽 끝 위치를 계산할 수 있습니다.
#
# 버섯 채집 총합 = 왼쪽 끝 ~ 오른쪽 끝 구간의 합.
#
# 이 합은 접두사 합을 이용해 O(1)로 계산

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    # 왼쪽으로 p번 이동하는 경우
    for p in xrange(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))

    # 오른쪽으로 p번 이동하는 경우
    for p in xrange(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result
