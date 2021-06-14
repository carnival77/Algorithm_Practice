from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

print(graph)

distance = [-1] * (n+1)
distance[x] = 0

que = deque()
que.append(x)

print(que)

while que:
    this_node = que.popleft()
    for new_node in graph[this_node]:
        if distance[new_node] == -1:
            distance[new_node] = distance[this_node] + 1
            que.append(new_node)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check=True

if check==False:
    print(-1)
