# 인접 행렬 사용
import sys

input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작점
matrix = [[0] * (N + 1) for i in range(N + 1)] # 정점의 개수 + 1
for i in range(M): # 간선의 개수
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit = [0] * (N + 1) # 정점의 개수 + 1


def dfs(matrix, V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if (visit[i] == 0 and matrix[V][i] == 1):
            dfs(matrix,i)


def bfs(matrix, V):
    queue = [V]
    visit[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if (visit[i] == 0 and matrix[V][i] == 1):
                visit[i] = 1
                queue.append(i)


dfs(matrix, V)
print()
visit = [0] * (N + 1) # 정점의 개수 + 1
bfs(matrix, V)

# 인접 리스트 활용
from collections import deque
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n+1):
    a[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()