# solution : 두 번째줄부터, 위의 행의 값들 중 자신의 열을 제외한 값들 중에서 최댓값을 더한다.
# 이것을 마지막 줄까지 반복하면, 마지막 줄에는 열의 중복 선택 없이 선택된 행이 나온다. 이 중 최댓값이 정답.

# solution 1 : DP를 활용
def solution(land):

    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])

    return max(land[-1])

# solution 2 : 완전 탐색
def solution2(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution2(land))