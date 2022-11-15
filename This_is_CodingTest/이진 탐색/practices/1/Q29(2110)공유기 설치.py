import sys

n,c = map(int,sys.stdin.readline().split(' '))

houses = []

for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

# 두 공유기 사이의 거리의 범위 설정.
start = 1 # 최소 gap
end = houses[-1] - houses[0] # houses에서 두 공유기 사이의 최대 거리(gap)
result = 0

while (start<=end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    installed_point = houses[0]  # 공유기가 설치된 지점
    count = 1  # houses[0] 에 이미 한 개 설치하고 시작

    for i in range(1, n):
        # 현재 공유기 사이의 거리로 설치 가능한 곳에 공유기 설치
        # houses[0]에 1개를 이미 설치했으므로 1부터 range 시작
        if houses[i] >= installed_point + mid: # 공유기 설치 가능한 거리에 있는 점에
            installed_point = houses[i] # 공유기 설치하고, 공유기 설치 지점 업데이트하여 현재 거리로 다음 공유기 설치할 곳 찾기
            count += 1 # 설치된 공유기 개수 증가

    # 공유기가 목표 c보다 적게 설치되었다면
    # 공유기 사이의 거리를 줄여 더 촘촘한 간격으로 설치 가능 지점을 탐색하고 설치해야 한다.
    # end = mid - 1 로 하여 범위를 줄여 mid 값을 줄인다.
    if count < c:
        end = mid - 1
    # 공유기가 목표 c보다 많거나 같게 설치되었다면
    # 두 공유기 사이의 최대 거리를 찾기 위해 공유기 사이의 거리를 늘려야 한다.
    # start = mid + 1 로 하여 범위를 늘려 mid 값을 늘려본다.
    # 그리고 result에 현재 mid, 즉 현재 두 공유기 사이의 최대 거리를 저장한다.
    else:
        start = mid + 1
        result = mid

print(result)