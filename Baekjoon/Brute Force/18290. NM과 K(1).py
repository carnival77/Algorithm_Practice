n,m,k = map(int,input().split())

board=[]
visited=[[False] * m for _ in range(n)]

for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

ans = -2147483647
cnt=0
sum=0

def recursive(px,py,cnt,sum):
    if cnt == k :
        global ans
        if ans<sum:
            ans=sum
        return

    for x in range(px,n):
        for y in range(py if x == px else 0, m):
            if visited[x][y]:
                continue
            possible = True

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        possible = False
            if possible:
                visited[x][y] = True
                recursive(x,y,cnt+1,sum+board[x][y])
                visited[x][y] = False

recursive(0,0,cnt,sum)
print(ans)