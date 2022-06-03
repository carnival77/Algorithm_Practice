# 현재 지점에서 다른 지점으로 넘어가면서 최단거리를 갱신할 때 다음 지점의 부모를 현재 지점으로 설정
# 경로를 출력해줄 때는 도착지점(5번 노드) -> 5번 노드의 부모(4번 노드) -> 4번 노드의 부모(1번 노드)를 역으로 출력해주면 됩니다.
import heapq

n=int(input())
m=int(input())
INF=int(1e9)

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())
ans=[]

parents=dict()

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for near_node_num,near_node_cost in graph[now]:
            cost=dist+near_node_cost
            if cost<distance[near_node_num]:
                distance[near_node_num]=cost
                heapq.heappush(q,(cost,near_node_num))
                parents[near_node_num]=now

dijkstra(start)

print(distance[end])
current=end
while current!=start:
    ans.append(current)
    current=parents[current]
ans.append(start)
ans.reverse()
print(len(ans))
print(*ans)

# 참고 : https://studyandwrite.tistory.com/381