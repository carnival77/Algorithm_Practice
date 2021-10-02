# 우선순위 큐 사용

import heapq


# 풀이 1 : try,except를 사용해, 음식을 pop하는 과정에서 오류 발생할 경우 개수가 부족해 발생한 것이므로 사실상 더 맵게 만들기는 불가능하므로 -1 리턴
def solution(scoville, K):

    answer = 0

    heapq.heapify(scoville)

    ok = True

    while scoville[0]<K:
        try:
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            new = a+2*b
            heapq.heappush(scoville,new)
        except:
            return -1

        answer+=1

    return answer

scoville=[1, 2, 3, 9, 10, 12]
K=7

print(solution(scoville,K))


# 풀이 2 - heappop을 하나 한 다음, 음식이 남아 있지 않아 더 이상 second 음식을 섞을 수 없는 경우 -1 리턴
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer