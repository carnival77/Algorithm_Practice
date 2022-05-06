dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램
def recur(step,x1,y1,x2,y2):
    # 버튼을 10번보다 많이 눌러야 한다면, -1 출력
    if step==11:
        return -1
    fall1=False
    fall2=False
    # 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
    if x1<0 or x1>=n or y1<0 or y1>=m:
        fall1=True
    if x2<0 or x2>=n or y2<0 or y2>=m:
        fall2=True
    # 두 동전을 떨어뜨릴 수 없으면 -1 출력
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans=-1

    for k in range(4):
        nx1,ny1,nx2,ny2=x1+dx[k],y1+dy[k],x2+dx[k],y2+dy[k]
        # 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
        if 0<=nx1<n and 0<=ny1<m and a[nx1][ny1]=='#':
            nx1, ny1 = x1,y1
        if 0<=nx2<n and 0<=ny2<m and a[nx2][ny2]=='#':
            nx2, ny2 = x2,y2
        temp=recur(step+1,nx1,ny1,nx2,ny2)
        if temp==-1:
            continue
        # 버튼의 최소 횟수를 출력
        if ans==-1 or ans>temp:
            ans=temp
    return ans

n,m=map(int,input().split())
x1=x2=y1=y2=-1 # 두 동전 위치
a=[list(input()) for _ in range(n)]
# 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.
for i in range(n):
    for j in range(m):
        if a[i][j]=='o': # 동전 위치 찾으면
            if x1==-1:
                x1,y1=i,j
            else:
                x2,y2=i,j
            a[i][j]='.' #  해당 칸은 빈 칸으로. 이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다라는 조건에 대해, 빈 칸으로 만들어줘서 더 편하게 탐색하기 위해
print(recur(0,x1,y1,x2,y2))