n,m=map(int,input().split())
a=[list(map(int,input())) for _ in range(n)]
b=[list(map(int,input())) for _ in range(n)]

cnt=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            cnt+=1
            for x in range(3):
                for y in range(3):
                    if a[i+x][j+y]==1:
                        a[i+x][j+y]=0
                    elif a[i+x][j+y]==0:
                        a[i+x][j+y]=1
if a==b:
    print(cnt)
else:
    print(-1)