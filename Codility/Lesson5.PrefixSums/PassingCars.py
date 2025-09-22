"""
아이디어: 0(동쪽) 수를 누적, 1(서쪽) 나오면 그때까지의 0 개수를 정답에 더함
시간: O(N), 공간: O(1)
"""

def solution(A):
    east = 0       # 지금까지 지나온 0(동쪽) 차량 수
    ans = 0

    for x in A:
        if x == 0:
            east += 1
        else:  # x == 1
            ans += east
            if ans > 1_000_000_000:
                return -1

    return ans
