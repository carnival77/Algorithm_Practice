import sys
input=sys.stdin.readline

n=int(input())
a=[[0]*n for _ in range(n)]
order=[]
likes=[0]*(n**2+1)
for i in range(n**2):
    data=list(map(int,input().split()))
    x=data[0]
    order.append(x)
    likes[x]=data[1:]
ans=0

dx=[-1,1,0,0]
dy=[0,0,1,-1]

for no in order:
    like=likes[no]
    cand = []
    for x in range(n):
        for y in range(n):
            if a[x][y]!=0: continue
            friends=0
            empty=0
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if a[nx][ny] in like:
                        friends+=1
                    if a[nx][ny]==0:
                        empty+=1
            cand.append([friends,empty,y,x])
    cand.sort(reverse=True)
    y,x=cand[0][2:]
    a[x][y]=no

for x in range(n):
    for y in range(n):
        no=a[x][y]
        like = likes[no]
        cnt=0
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] in like:
                    cnt+=1
        if cnt>=1:
            ans+=10**(cnt-1)

print(ans)