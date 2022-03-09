from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)

for i in range(1,n+1):
    graph[i].sort()

visited = [False]*(n+1)
dist=[0]*(n+1)

ok=False

visited[x] = True
q=deque()
q.append(x)
while q:
    x=q.popleft()
    for y in graph[x]:
        if visited[y]==False:
            visited[y]=True
            q.append(y)
            dist[y]=dist[x]+1


for i in range(1,n+1):
    if dist[i]==k:
        print(i)
        ok=True

if ok==False:
    print(-1)