from collections import deque

input_n,q = map(int,input().split())
n=2**input_n
a=[list(map(int,input().split())) for _ in range(n)]
ls=list(map(int,input().split()))
dx=[-1,0,1,0]
dy=[0,-1,0,1]

# 매트릭스 시계방향 90도 회전
def rotate_clock_90(b):
    n2=len(b)
    c=[[0]*n2 for _ in range(n2)]

    for i in range(n2):
        for j in range(n2):
            c[i][j]=b[n2-1-j][i]
    return c

# 전체 매트릭스 중 가로 세로 sub_size 인 부분 매트릭스를 부분 분할하고, 그것을 시계방향으로 90도 회전한 뒤 전체 매트릭스에 변경 내용 적용
def process(sx,sy,sub_size):
    # 부분 매트릭스
    part=[[0]*sub_size for _ in range(sub_size)]

    # 전체로부터 부분 분할
    for i in range(sub_size):
        for j in range(sub_size):
            part[i][j]=a[sx+i][sy+j]

    # 부분 매트릭스 시계방향 90도 회전
    rotated_part = rotate_clock_90(part)

    # 부분 매트릭스 변경 내용 전체 매트릭스에 적용
    for i in range(sub_size):
        for j in range(sub_size):
            a[sx+i][sy+j]=rotated_part[i][j]

# 각 시행마다
for l in ls:
    # 부분 매트릭스 크기 설정
    sub_size=2**l
    for x in range(0,n,sub_size):
        for y in range(0,n,sub_size):
            # 전체 매트릭스 중 가로 세로 sub_size 인 부분 매트릭스를 부분 분할하고, 그것을 시계방향으로 90도 회전한 뒤 전체 매트릭스에 변경 내용 적용
            process(x,y,sub_size)

    # 인접한 칸 중 얼음 칸이 3개 이상이면 변화 X. 3개 미만이면 얼음 -1
    # 이때, 전체 2차원 배열의 (0,0)칸부터 탐색하며 차례대로 처리하는 것이 아닌, 탐색 전의 원래 상태를 기준으로 처리 후보를 뽑은 후 그 후보들을 처리해줘야 한다.
    cand=deque()
    for x in range(n):
        for y in range(n):
            cnt=0
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<n and 0<=ny<n and a[nx][ny]>0:
                    cnt+=1
            if cnt<3 and a[x][y]>0:
                cand.append((x,y))

    while cand:
        x,y=cand.popleft()
        a[x][y]-=1

# 남아있는 얼음 A[r][c]의 합, 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
total=0
max_cnt=0
visit=[[False] * n for _ in range(n)]

def bfs(sx,sy):
    global max_cnt, total
    q=deque()
    q.append((sx,sy))
    visit[sx][sy]=True
    cnt=1
    total+=a[sx][sy]
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and a[nx][ny]>0:
                q.append((nx,ny))
                visit[nx][ny]=True
                cnt += 1
                total+=a[nx][ny]

    max_cnt=max(cnt,max_cnt)

for x in range(n):
    for y in range(n):
        if not visit[x][y] and a[x][y]>0:
            bfs(x,y)

print(total)
print(max_cnt)