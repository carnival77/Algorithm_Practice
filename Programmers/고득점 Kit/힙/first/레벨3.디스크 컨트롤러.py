import heapq

def solution(jobs):
    answer = 0

    now,i=0,0
    start=-1
    heap=[]
    n=len(jobs)

    while i<n:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        if heap:
            cur = heapq.heappop(heap)
            start=now
            now += cur[0]
            answer += now-cur[1]
            i+=1
        else:
            now+=1

    return int(answer/n)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

## 참고
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99