from copy import deepcopy

n=4
# 상하좌우, 대각선
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

num = [[0] * n for _ in range(n)] # 물고기 위치
direction = [[0] * n for _ in range(n)] # 물고기 방향

# 물고기 정보 insert
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(4):
        num[i][j] = row[2*j]
        direction[i][j] = row[2*j+1]
        direction[i][j]-=1

def dfs(num,direction,x,y,d): # num,direction, 상어 위치 x,y, 방향
    # 물고기 이동
    for fish in range(1,n*n+1): # 물고기 번호 1~16번 차례로
        find=False # 이번에 찾아야 할 물고기를 찾으면 True
        for i in range(n):
            for j in range(n):
                if num[i][j] == fish: # 물고기 찾았으면
                    for k in range(8): # 이동 가능한 지 8방향으로 확인
                        nx,ny = i+dx[direction[i][j]],j+dy[direction[i][j]]
                        if 0<=nx<n and 0<=ny<n and (not (nx == x and ny == y)): # 범위 내이고, 상어 위치가 아니라면 이동 가능
                            num[i][j],num[nx][ny] = num[nx][ny],num[i][j]
                            direction[i][j],direction[nx][ny] = direction[nx][ny],direction[i][j]
                            find=True
                            break
                        else: # 이둥 볼가라면 방향 돌리기
                            direction[i][j]+=1
                            direction[i][j]%=8
                if find:
                    break
            if find:
                break

    # 상어 이동
    ans=0
    sx=x+dx[d]
    sy=y+dy[d]
    while 0<=sx<n and 0<=sy<n: # 상어가 이동 가능한 범위 내라면
        if num[sx][sy] != 0: # 이동한 칸에 물고기 있으면
            temp=num[sx][sy]
            num[sx][sy]=0
            # 이동한 칸의 물고기를 먹은 이후 전개될 물고기의 이동과 상어의 이동 등을 dfs로 전개.
            # 그리고 그 값을 cur에 저장한다. 그 전개 도중 num을 계속 바꾸는 것이 아닌,
            # 이 라인 직전까지 전개된 num 배열의 상태를 dfs로 넘겨주어, 각각의 전개가 서로에게 영향을 미치지 않게 한다.
            cur = temp + dfs(deepcopy(num),deepcopy(direction),sx,sy,direction[sx][sy])
            # cur들 중 최댓값을 ans로 설정한다.
            if ans<cur:
                ans=cur
            num[sx][sy]=temp
        sx+=dx[d]
        sy+=dy[d]

    return ans


x,y=0,0 # 초기 상어 위치
ans = num[x][y] # 초기 상어
num[x][y] = 0 # 물고기가 없으면 0
ans+=dfs(num,direction,x,y,direction[x][y])
print(ans)