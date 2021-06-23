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

    for i in range(1, n): # houses[0]에 1개를 이미 설치했으므로 1부터 range 시작
        if houses[i] >= installed_point + mid:
            installed_point = houses[i]
            count += 1

    # 공유기가 목표 c보다 적게 설치되었다면 end = mid - 1 로 하여 범위를 줄여 mid 값을 줄인다.
    if count < c:
        end = mid - 1
    # 공유기가 목표 c보다 많거나 같게 설치되었다면 start = mid + 1 로 하여 범위를 늘려 mid 값을 늘려본다.
    # 그리고 result에 현재 mid, 즉 현재 두 공유기 사이의 최대 거리를 저장한다.
    else:
        start = mid + 1
        result = mid

print(result)