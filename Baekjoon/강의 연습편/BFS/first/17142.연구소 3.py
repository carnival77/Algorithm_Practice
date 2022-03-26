# solution 2. combinations 대신 dfs 사용하여 board의 2 지점들 중 m개를 선택
from collections import deque
import sys

n,m = map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 바이러스가 퍼질 위치 후보
subs=[]
ans=-1

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            # board[i][j]=0
            subs.append((i,j))

def bfs():
    # m개가 선택된 후,
    q=deque()
    # 각 칸에 도달하기 위한 최단 거리를 업데이트한다.
    d=[[-1] * n for _ in range(n)]

    # m개 지점을 큐에 넣는다.
    for i in range(n):
        for j in range(n):
            # 활성 바이러스면 큐에 넣는다.
            if board[i][j] == 3:
                q.append((i,j))
                # 해당 지점부터 바이러스가 시작되도록 d 를 0 으로 바꾼다
                d[i][j]=0
            # # 비활성 바이러스면 활성 바이러스가 오면 해당 지점부터 바이러스가 시작되도록 d 를 0 으로 바꾼다
            # elif board[i][j] == 2:
            #     d[i][j] = 0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n :
                # d로 해당 칸에 방문했는 지 아닌 지 판별
                if board[nx][ny] != 1 and d[nx][ny] == -1:
                    # 그러므로 여기서 board 의 숫자를 바꿀 필요 없다
                    # # 비활성 바이러스면 활성 바이러스가 오면 해당 지점부터 바이러스가 시작되도록 d 를 0 으로 바꾼다
                    # if board[nx][ny] == 2:
                    #     d[nx][ny] = 0
                    #     q.append((nx, ny))
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1


    # 이번 bfs의 최소 시간을 cur로
    cur=0
    for i in range(n):
        for j in range(n):
            # 빈 칸. 즉, 처음부터 바이러스가 없던 칸들에
            if board[i][j] == 0:
                # 그런데 방문하지 않은 칸이 있다면 ans를 -1로 유지하기 위해 return
                if d[i][j] == -1:
                    return
                # 빈 칸. 즉, 처음부터 바이러스가 없던 칸들이 모두 방문한 칸들이라면, 이번 bfs의 최소 시간을 cur로
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    # ans 는 모든 cur 중에 최솟값
    if ans == -1 or ans > cur:
        ans=cur


# dfs 로 후보들 중 m개를 고르고, 설치하고(3으로 바꿔서), 다시 부순다(2으로 바꾼다).
def go(index,cnt):
    # index가 모든 후보를 다 탐색했을 때,
    if index == len(subs):
        # 설치된 개수가 m 개일 때
        if cnt == m:
            # 바이러스를 퍼뜨린다
            bfs()
    else:
        x,y = subs[index]
        # 활성 바이러스가 있는 곳을 3으로 바꾼다
        board[x][y] = 3
        cnt+=1
        go(index+1,cnt)
        # 다시 돌려놓는다.
        board[x][y] = 2
        # board[x][y]=0
        cnt-=1
        go(index+1,cnt)

go(0,0)
print(ans)

