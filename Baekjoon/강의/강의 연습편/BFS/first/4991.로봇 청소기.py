# solution 1. 시간 초과. 중복되는 탐색 루트를 줄이기 못했다. 시간 복잡도 10! x 20*20 x 10 >= 120억
# from collections import deque
# from itertools import permutations
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# while True:
#     ans=1e9
#     m,n=map(int,input().split())
#     if (m,n)==(0,0):
#         break
#     a=[list(input()) for _ in range(n)]
#     d=[[-1]*m for _ in range(n)]
#     sx,sy=0,0
#     t=[]
#     for i in range(n):
#         for j in range(m):
#             if a[i][j]=='o':
#                 sx,sy=i,j
#             if a[i][j]=='*':
#                 t.append((i,j))
#     d[sx][sy]=0
#     q=deque()
#     q.append((sx,sy))
#     ok=False
#
#     for order in permutations(t,len(t)):
#         d = [[-1] * m for _ in range(n)]
#         d[sx][sy] = 0
#         q = deque()
#         q.append((sx, sy))
#         res=0
#         tmp=t[:]
#         for tx,ty in order:
#             while q:
#                 x, y = q.popleft()
#                 if x==tx and y==ty:
#                     tmp.remove((x,y))
#                     res+=d[x][y]
#                     d = [[-1] * m for _ in range(n)]
#                     d[x][y]=0
#                     q.clear()
#                     q.append((x,y))
#                     break
#
#                 for k in range(4):
#                     nx, ny = x + dx[k], y + dy[k]
#                     if 0 <= nx < n and 0 <= ny < m:
#                         if a[nx][ny] != 'x' and d[nx][ny] == -1:
#                             if a[nx][ny]=='*':
#                                 if nx==tx and ny==ty:
#                                     q.append((nx, ny))
#                                     d[nx][ny] = d[x][y] + 1
#                             else:
#                                 q.append((nx, ny))
#                                 d[nx][ny] = d[x][y] + 1
#         ans=min(ans,res)
#         if not tmp or ok:
#             ok=True
#
#     if not ok:
#         print(-1)
#     else:
#         print(ans)

# solution 2. 중복되는 탐색 루트 제거. 시간 복잡도 10! x 10 = 36288000 = 약 3천만
# 해설
# 문제의 관건은 중복되는 탐색 루트를 줄이는 것이다.
# 문제 유형은 브루트 포스 + BFS인데, 더러운 곳의 개수가 10개 미만이고, 격자 칸의 최대 크기는 20*20이므로, 만일 10개의 더러운 칸으로 만드는 순열의 조합 각각의 경우 BFS 탐색을 한다고 하면, 최악의 경우 시간 복잡도 10! x 20*20  >= 12억이다.
# 따라서 중복되는 탐색 루트를 제거할 필요가 있다.
# 시작점에서부터 더러운 곳을 차례로 방문하는 경우의 최단 거리는 중복된다.
# 가령, 더러운 곳이 3 곳이고, 그 번호를 1,2,3으로 하며, 더러운 곳과 시작점을 모두 정점이라고 한다면, 모든 순열의 경우의 수는
# 시작점 -> 1 -> 2 -> 3
# 시작점 -> 1 -> 3 -> 2
# 시작점 -> 2 -> 1 -> 3
# 시작점 -> 2 -> 3 -> 1
# 시작점 -> 3 -> 1 -> 2
# 시작점 -> 3 -> 2 -> 1
# 인데, 여기서 시작점 -> 1, 1 -> 2, 2 -> 3 과 같은 루트들이 중복된다.
# 따라서 초기 BFS 탐색 한 번으로 정점 간의 최단 거리를 배열 d에 저장하면, 각 순열의 경우의 수에서 정점 간에 최단 거리를 구하기 위해 매번 BFS를 수행하지 않아도 된다.
from collections import deque
from itertools import permutations
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    b=[(0,0)] # 더러운 곳과 시작점을 모두 정점으로 갖는 배열
    for i in range(n):
        for j in range(m):
            if a[i][j]=='o':
                b[0]=(i,j) # 시작점을 배열의 첫 번째 요소로 갖는다.
            elif a[i][j]=='*':
                b.append((i,j))
    l=len(b)
    d=[[0]*l for _ in range(l)] # 정점 간에 최단 거리를 저장한 배열
    ok=True
    for i in range(l):
        dist=bfs(a,b[i][0],b[i][1])
        for j in range(l):
            d[i][j]=dist[b[j][0]][b[j][1]]
            if d[i][j]==-1: # 만약 한 번이라도 탐색할 수 없는 경우가 나오면 -1  출력
                ok=False
                break
    if not ok:
        print(-1)
        continue
    p=[i+1 for i in range(l-1)] # 시작점은 제외
    ans=1e9
    for permu in permutations(p,len(p)): # 시작점을 제외한 정점들의 인덱스를 순열로 만든다.
        res=d[0][permu[0]]
        for i in range(l-2):
            res+=d[permu[i]][permu[i+1]]
        ans=min(ans,res)
    print(ans)