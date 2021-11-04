import heapq

INF=int(1e9)

def solution(N, road, K):
    answer = 0
    n=N
    start=1

    graph=[[] for i in range(n+1)]

    distance=[INF]*(n+1)

    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a, c))

    def dijkstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0

        while q:
            min_dist,now = heapq.heappop(q)

            if distance[now] < min_dist:
                continue

            for next,next_dist in graph[now]:
                cost = min_dist+next_dist
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q,(cost,next))

    dijkstra(start)

    for i in distance:
        if i<=K:
            answer+=1

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))