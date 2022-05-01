# first try : 클래스 이용. 하지만 디버깅이 어렵다.

# class Shark:
#     def __init__(self,n,d,up,left,down,right,x,y):
#         self.n=n
#         self.d=d
#         self.up=up
#         self.down=down
#         self.left=left
#         self.right=right
#         self.x=x
#         self.y=y
#
# #상, 하, 좌, 우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# n,m,k=map(int,input().split())
# a=[list(map(int,input().split())) for _ in range(n)]
# b = [[[] for j in range(n)] for i in range(n)]
# dirs=list(map(int,input().split()))
# pri=[]
# for i in range(m):
#     shark=[]
#     for j in range(4):
#         shark.append(map(int,input().split()))
#     pri.append(shark)
# smell=[[0]*n for _ in range(n)]
# smell_who=[[0]*n for _ in range(n)]
#
# for x in range(n):
#     for y in range(n):
#         if a[x][y]!=0:
#             # print(a[x][y])
#             b[x][y].append(Shark(a[x][y],dirs[a[x][y]-1],pri[a[x][y]-1][0],pri[a[x][y]-1][1],pri[a[x][y]-1][2],pri[a[x][y]-1][3],x,y))
#             # a[x][y]=(Shark(a[x][y],dirs[a[x][y]-1],pri[a[x][y]-1][0],pri[a[x][y]-1][1],pri[a[x][y]-1][2],pri[a[x][y]-1][3],x,y))
#
# def get_priority(shark):
#     d=shark.d
#     if d==1: #상
#         return shark.up
#     elif d==2: #하
#         return shark.down
#     elif d==3: #좌
#         return shark.left
#     else: #우
#         return shark.right
#
# def move(shark):
#     priority=get_priority(shark)
#     ok=False
#     #2.1
#     for pd in priority:
#         pd-=1
#         nx,ny=x+dx[pd],y+dy[pd]
#         if 0<=nx<n and 0<=ny<n and smell[nx][ny]==0:
#             b[x][y].remove(shark)
#             shark.x,shark.y=nx,ny
#             b[nx][ny].append(shark)
#             ok=True
#         if ok:
#             break
#     #2.2
#     for pd in priority:
#         pd -= 1
#         nx, ny = x + dx[pd], y + dy[pd]
#         if 0 <= nx < n and 0 <= ny < n and smell_who[nx][ny]==shark.n:
#             b[x][y].remove(shark)
#             shark.x, shark.y = nx, ny
#             b[nx][ny].append(shark)
#             break
#
# def kickout(sharks):
#     global m
#     sharks.sort(key=lambda shark:shark.n)
#     while True:
#         cnt=len(sharks)
#         if cnt==1:
#             break
#         sharks.pop()
#         m-=1
#
# for t in range(1,1001):
#
#     #1. 각 상어가 자신의 위치에 냄새 뿌리기
#     for x in range(n):
#         for y in range(n):
#             if len(b[x][y])>0:
#                 shark=b[x][y][0]
#                 shark_num=shark.n
#                 smell_who[x][y]=shark_num
#                 smell[x][y]=k
#
#     for i in range(n):
#         elements=[]
#         for j in range(n):
#             if len(b[i][j])>0:
#                 for a in b[i][j]:
#                     elements.append(a.n)
#
#
#
#     for i in range(n):
#         print(smell[i])
#
#     for i in range(n):
#         print(smell_who[i])
#
#     #2. 상어 이동
#     for x in range(n):
#         for y in range(n):
#             if len(b[x][y])>0:
#                 shark=b[x][y][0]
#                 move(shark)
#
#     #3. 같은 칸에서 번호 높은 상어 쫓아내고 번호 낮은 상어 하나만 남기기
#     for x in range(n):
#         for y in range(n):
#             if len(b[x][y])>0:
#                 kickout(b[x][y])
#
#     #4. 냄새 제거
#     for x in range(n):
#         for y in range(n):
#             if smell[x][y]>0:
#                 smell[x][y]-=1
#
#     #5. 번호 1인 상어 한 마리만 남았을 때 중지
#     if m==1:
#         print(t)
#         break

#1. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
#2.  그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
#2.1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
#2.2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
#3.  1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지

#상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,smell_time = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
shark=[[0]*n for _ in range(n)] # 상어 번호별 위치
shark_next=[[0]*n for _ in range(n)] # 다음에 위치하게 될 상어의 위치
smell=[[0]*n for _ in range(n)] # 냄새
smell_who=[[0]*n for _ in range(n)] # 누구의 냄새?
priority = [[[0]*4 for _ in range(4)] for __ in range(m+1)] # priority[i][j][k] : i번 상어의 방향이 j일 때 4개의 우선 순위 중 k번째 방향
#  우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.

for x in range(n):
    for y in range(n):
        if a[x][y]>0:
            shark[x][y]=a[x][y]
            smell[x][y]=smell_time
            smell_who[x][y]=a[x][y]

dirs=[0]+[d-1 for d in map(int,input().split())] # 상어의 번호별 현재 방향

for i in range(1,m+1):
    for j in range(4):
        priority[i][j]=[d-1 for d in map(int,input().split())]

#3. 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
def check_1():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if shark[i][j] > 0:
                cnt += 1
    return cnt == 1

#2. 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
def move():
    sharks=[]
    for x in range(n):
        for y in range(n):
            shark_next[x][y]=0 # 다음에 위치하게 될 상어의 위치를 0으로 초기화한다.
            if shark[x][y]>0:
                sharks.append((shark[x][y],x,y))

    sharks.sort() # 번호가 작은 상어부터 움직인다.

    for s in sharks:
        num,sx,sy = s # 상어의 번호와 위치
        shark_d = dirs[num] # 상어의 현재 방향
        ok=False # 이동해야 할 칸 찾았으면 True

        for k in range(4): # 4가지 방향 중에서, 해당 상어의 번호에 부여된 우선 순위에서 현재 방향에 맞는 순위를 순차적으로 탐색한다.
            pd=priority[num][shark_d][k] #  우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
            nx=sx+dx[pd]
            ny=sy+dy[pd]
            #2.1. 인접한 칸 중 아무 냄새가 없는 칸 찾기
            if 0<=nx<n and 0<=ny<n and smell[nx][ny]==0:
                # 만약 이동할 칸에
                # 상어가 없다면
                if shark_next[nx][ny]==0:
                    shark_next[nx][ny]=num
                    dirs[num]=pd
                # 상어가 있는데, 현재 상어보다 번호가 크면 쫓겨난다
                else:
                    if shark_next[nx][ny]>num:
                        shark_next[nx][ny]=num
                        dirs[num]=pd
                # 이동했으면 방향 탐색 종료
                ok=True
                break

        # 2.1. 에서 이동 안 했으면,
        # 2.2. 자신의 냄새가 있는 칸의 방향으로 잡는다.
        if not ok:
            for k in range(4):
                pd = priority[num][shark_d][k]
                nx = sx + dx[pd]
                ny = sy + dy[pd]
                # 2.2. 인접한 칸 중 자신의 냄새가 있는 칸 찾기
                if 0 <= nx < n and 0 <= ny < n and smell[nx][ny] > 0 and smell_who[nx][ny]==num:
                    shark_next[nx][ny] = num
                    dirs[num] = pd
                    # 이동했으면 종료
                    ok = True
                    break

    for x in range(n):
        for y in range(n):
            # shark_next 에 저장되어 있는 예정된 칸으로 상어를 이동.
            shark[x][y]=shark_next[x][y]
            # smell 1씩 빼기
            if smell[x][y]>0:
                smell[x][y]-=1
            # smell 0 이면 smell_who 도 0으로
            if smell[x][y]==0:
                smell_who[x][y]=0
            # 상어 있는 칸에 smell, smell_who 상어 정보 및 smell_time으로 초기화
            if shark[x][y]>0:
                smell_who[x][y]=shark[x][y]
                smell[x][y]=smell_time
ans = -1
for t in range(1,1001):
    move()
    if check_1():
        ans = t
        break
print(ans)