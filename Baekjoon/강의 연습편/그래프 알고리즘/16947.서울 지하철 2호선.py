import sys

sys.setrecursionlimit(1000000)
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

check = [0] * n  # 0: not visited, 1: visited, 2: cycle


def go(x, p):
    # -2: found cycle and not included
    # -1: not found cycle
    # 0~n-1: found cycle and start index

    if check[x] == 1:
        return x

    check[x] = 1
    for y in a[x]:
        if y == p:
            continue
        res = go(y, x)
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res:
                return -2
            else:
                return res
    return -1


go(0, -1)

q = deque()
dist = [-1] * n

for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(*dist, sep=' ')