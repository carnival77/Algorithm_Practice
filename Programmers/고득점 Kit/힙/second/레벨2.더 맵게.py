import heapq

def solution(scoville, K):
    answer=0

    heapq.heapify(scoville)

    while scoville[0]<K:
        try:
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            heapq.heappush(scoville,a+b*2)
        except:
            return -1
        answer+=1

    return answer

scoville=[1, 2, 3, 9, 10, 12]
K=7
print(solution(scoville,K))