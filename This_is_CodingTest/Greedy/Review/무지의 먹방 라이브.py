import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    # heapq 는 heap 구조로 큐를 변화시킨다.
    # 힙은 일종의 반정렬 상태(느슨한 정렬 상태) 를 유지한다.
    # 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도
    # 간단히 말하면 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰(작은) 이진 트리를 말한다.
    # https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
    #
    # 여기서 heap은 최소힙으로, 최소 힙(min heap)
    # 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
    # https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    # 즉, 늘 첫 번째 요소가 최솟값이란 것을 보장한다.

    # 먹는 시간 합
    sum_time = 0
    # 이전에 먹는 시간
    pre_time = 0

    # 음식 개수
    food_cnt = len(food_times)

    # 사이클 = 먹는 시간 합 + (먹는 시간이 최소로 걸리는 음식의 먹는 시간 - 이전 음식의 먹는 시간) * 음식 개수
    # 사이클 (먹는 시간 합 + (먹는 시간이 최소로 걸리는 음식의 먹는 시간 - 이전 음식의 먹는 시간) * 음식 개수) 반복 <= k
    # 이렇게 하면 k 시간이 될 때까지, 먹는 시간이 최소로 걸리는 음식부터 차례로 먹어서 0으로 만들고 리스트에서 제외할 수 있다.
    while sum_time + (q[0][0] - pre_time) * food_cnt <= k:
        # 이번에 먹을 음식의 먹는 시간 = 먹는 시간이 최소로 걸리는 음식의 먹는 시간
        this_food_time = heapq.heappop(q)[0]
        # 먹는 시간의 합에 (먹는 시간이 최소로 걸리는 음식의 먹는 시간 - 이전 음식의 먹는 시간) * 음식 개수 를 더한다
        sum_time += (this_food_time - pre_time) * food_cnt
        # 음식 하나를 다 먹었으니 음식 개수 -1
        food_cnt -= 1
        # 다음으로 먹는 시간이 최소인 음식을 고르기 전에 이전에 먹는 시간에 이번 음식의 먹는 시간을 넣는다.
        pre_time = this_food_time

    # k초 이전의 사이클 동안 최대한 음식을 먹고난 후, 남은 음식들을 번호 순으로 정렬한다.
    result = sorted(q, key=lambda x: x[1])
    # 번호 순 정렬된 음식들 중 남은 음식들 중에서, 남은 시간의 마지막에 먹게 될 음식의 번호를 구한다.
    return result[(k - sum_time) % food_cnt][1]
