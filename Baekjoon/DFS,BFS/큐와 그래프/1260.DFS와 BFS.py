import sys

input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit = [0] * (N + 1)


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
visit = [0] * (N + 1)
bfs(matrix, V)