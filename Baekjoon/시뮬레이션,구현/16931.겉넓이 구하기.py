# 솔루션 : 3차원으로 생각하자. 2차원에서 dx,dy, nx,ny 를 쓰는 것처럼, 3차원으로 dx,dy,dz, nx,ny,nz를 써서 해결하자

n,m = map(int,input().split())

a=[]

for i in range(n):
    a.append(list(map(int,input().split())))

ans=0

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

MAX = 102

# 최대 3차원 공간 생성. 칸이 존재하면 True
blocks = [[[False] * MAX for _ in range(MAX)] * 102 for _ in range(MAX)]

# 칸 채우기
for i in range(n):
    for j in range(m):
        # 해당 칸에 쌓여있는 블록의 개수
        block_cnt = a[i][j]
        for k in range(1,block_cnt+1):
            # 블록 쌓기는 1칸부터 시작
            blocks[i+1][j+1][k] = True

# 다른 블록과 접하지 않은 면이 있으면 겉넓이 +1
ans=0
# 블록 쌓기는 1칸부터 시작하니 탐색도 1부터 n+1까지
for x in range(1,n+1):
    for y in range(1,m+1):
        # 해당 칸에 쌓여있는 블록의 개수
        block_cnt = a[x-1][y-1]
        for z in range(1,block_cnt+1):
            # 동서남북위아래 6방향 다 조사
            for d in range(6):
                nx=x+dx[d]
                ny=y+dy[d]
                nz=z+dz[d]
                # 만약 접한 칸이 비어있다면, 겉넓이 +1
                if blocks[nx][ny][nz] == False:
                    ans+=1

print(ans)