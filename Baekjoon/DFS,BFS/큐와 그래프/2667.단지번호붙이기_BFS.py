from collections import deque

n = int(input())
board=[]

for i in range(n):
    board.append(list(map(int,input())))

index=2
ans=[]
num=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(start,index):
    q=deque()
    q.append(start)
    global num

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = index
                num+=1
                q.append((nx,ny))

    return False

total=0

for i in range(n):
    for j in range(n):
        if(board[i][j] == 1):
            if(bfs((i,j),index)):
                total+=1
            index+=1
            ans.append(num)
            num=0

print(total)
ans.sort()
for i in ans:
    print(i)