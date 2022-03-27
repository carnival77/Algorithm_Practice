# d[i][j] : (i,j)로 이동할 때 가져올 수 있는 최대 사탕 개수

# 방법 1. d[i][j] 칸에 어디에서 올 수 있는 지

n,m=map(int,input().split())

d=[[0]*(m+1) for _ in range(n+1)]

a=[[0]*(m+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j],d[i][j-1],d[i-1][j-1])+a[i][j]

print(d[n][m])

# 방법 2. d[i][j] 칸에서 어디로 갈 수 있는 지

n,m = map(int,input().split())
a = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
d[1][1] = a[1][1]
for i in range(1, n+1):
    for j in range(1, m+1):
        if j+1 <= m and d[i][j+1] < d[i][j] + a[i][j+1]:
            d[i][j+1] = d[i][j] + a[i][j+1]
        if i+1 <= n and d[i+1][j] < d[i][j] + a[i+1][j]:
            d[i+1][j] = d[i][j] + a[i+1][j]
        if i+1 <= n and j+1 <= m and d[i+1][j+1] < d[i][j] + a[i+1][j+1]:
            d[i+1][j+1] = d[i][j] + a[i+1][j+1]
print(d[n][m])

# 방법 3. 대각선은 무시. 왜냐하면 대각선 이동은 가로-세로하고 난 후 이동보다 같거나 작을 것이기에

n,m = map(int,input().split())
a = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i-1][j],d[i][j-1])+a[i][j]
print(d[n][m])

# 방법 4. 탑다운 방식의 방법 1.

import sys
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
a = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
d = [[-1]*(m+1) for _ in range(n+1)] # -1로 초기화한다. 시간 초과 방지.
def go(i,j):
    if i < 1 or j < 1:
        return 0
    if d[i][j] >= 0:
        return d[i][j]
    d[i][j] = max(go(i-1,j),go(i,j-1))+a[i][j]
    return d[i][j]
print(go(n,m))

# 방법 5. 탑다운 방식의 방법 2.

import sys
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
a = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
d = [[-1]*(m+1) for _ in range(n+1)]
def go(i,j):
    if i > n or j > m:
        return 0
    if d[i][j] >= 0:
        return d[i][j]
    d[i][j] = max(go(i+1,j),go(i,j+1))+a[i][j]
    return d[i][j]
print(go(1,1))