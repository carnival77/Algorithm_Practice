import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []

    #
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_time = 0
    pre_time = 0

    food_cnt = len(food_times)

    while sum_time + (q[0][0] - pre_time) * food_cnt <= k:
        this_food_time = heapq.heappop(q)[0]
        sum_time += (this_food_time - pre_time) * food_cnt
        food_cnt -= 1
        pre_time = this_food_time

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_time) % food_cnt][1]
