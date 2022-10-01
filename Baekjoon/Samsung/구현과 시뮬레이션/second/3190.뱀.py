n=int(input())

k=int(input())

apples=[]
for i in range(k):
    apples.append(list(map(int,input().split())))

l=int(input())

changes=[]
for i in range(l):
    x,c=input().split()
    changes.append([int(x),c])

#위,오른쪽,아래,왼쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]

dir=1 #오른쪽

a=list([0] * n for _ in range(n))

# 사과가 있으면 1
for x,y in apples:
    a[x-1][y-1] = 1

x,y=0,0
time=0
i=0
a[x][y]=2
answer=0
q=[(x,y)]
while True:
    nx,ny = x+dx[dir],y+dy[dir]

    if 0<=nx<n and 0<=ny<n:
        if a[nx][ny] == 1:
            a[nx][ny]=2
            q.append((nx,ny))
        elif a[nx][ny]==2:
            answer=time+1
            break
        else:
            a[nx][ny]=2
            q.append((nx,ny))
            px,py=q.pop(0)
            a[px][py]=0
    else:
        answer=time+1
        break

    x,y=nx,ny
    time += 1

    if i<l:
        if time==changes[i][0]:
            c=changes[i][1]
            if c == 'L':
                dir-=1
                if dir==-1:
                    dir=3
            else:
                dir=(dir+1)%4
            i+=1


print(answer)