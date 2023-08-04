import sys
input=sys.stdin.readline

n,m,k,c=map(int,input().split())

a1=[list(map(int,input().split())) for _ in range(n)] # 나무 및 벽 맵
a3=[[0]*n for _ in range(n)] # 제초제 맵

ans=0

dx=[-1,0,1,0]
dy=[0,1,0,-1]
directions=[[-1,-1],[1,-1],[-1,1],[1,1]] # 대각선 4방향

for year in range(m):
    # 맵에 나무가 있는지 판별
    if max(map(max, a1))<=0:
        break
    # 나무 성장. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
    for x in range(n):
        for y in range(n):
            if a1[x][y]>0:
                cnt=0
                for d in range(4):
                    nx,ny=x+dx[d],y+dy[d]
                    if (0<=nx<n and 0<=ny<n) and a1[nx][ny]>0:
                            cnt+=1
                a1[x][y]+=cnt
    # 나무 번식. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다. 이때 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식이 되며, 나눌 때 생기는 나머지는 버립니다. 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
    a2 = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if a1[x][y]>0:
                cnt=0
                near=[]
                for d in range(4):
                    nx,ny=x+dx[d],y+dy[d]
                    if (0<=nx<n and 0<=ny<n) and a3[nx][ny]==0 and a1[nx][ny]==0:
                        cnt+=1
                        near.append([nx,ny])
                if cnt>0:
                    t=a1[x][y]//cnt
                    for nx,ny in near:
                        a2[nx][ny]+=t
    for x in range(n):
        for y in range(n):
            a1[x][y]+=a2[x][y]
    # 제초제 뿌릴 칸 선별
    # 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    # 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만,
    # 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
    # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우,
    # 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
    a2 = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if a1[x][y]<=0:
                continue
            a2[x][y]+=a1[x][y]
            for d1,d2 in directions:
                for i in range(1,k+1):
                    nx=x+d1*i
                    ny=y+d2*i
                    if (0<=nx<n and 0<=ny<n) and a1[nx][ny]>0:
                        a2[x][y]+=a1[nx][ny]
                    else:
                        break
    max_val=max(map(max,a2))
    # 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.
    cand=[]
    for x in range(n):
        for y in range(n):
            if a2[x][y]==max_val:
                cand.append([x,y])
    max_x,max_y=sorted(cand)[0]
    # 1년 이상일 경우, 기존 제초제 기간 -1
    # 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
    if year>=1:
        for x in range(n):
            for y in range(n):
                if a3[x][y]>0:
                    a3[x][y]-=1
    # 제초제 뿌리기. 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
    if a1[max_x][max_y]==0:
        a3[max_x][max_y]=c
        continue
    ans+=a1[max_x][max_y]
    a1[max_x][max_y]=0
    a3[max_x][max_y]=c
    for d1, d2 in directions:
        for i in range(1, k + 1):
            nx = max_x + d1 * i
            ny = max_y + d2 * i
            if (0 <= nx < n and 0 <= ny < n):
                a3[nx][ny] = c
                if a1[nx][ny] > 0:
                    ans += a1[nx][ny]
                    a1[nx][ny] = 0
                else:
                    break
print(ans)