n,m,x,y,k = map(int,input().split())

b=[[0] * m for i in range(n)]

for i in range(n):
    data=list(map(int,input().split()))
    for j in range(m):
        b[i][j]=data[j]

cmds=list(map(int,input().split()))

a1=[0,0,0,0,0,0,0]
a2=[0,0,0,0,0,0,0]

def process(a2, x, y):
    global b

    print(a2[1])

    if b[x][y]==0:
        b[x][y]=a2[6]
    else:
        a2[6]=b[x][y]
        b[x][y]=0

    return a2

for cmd in cmds:
    if cmd == 1:
        ny=y+1
        if 0<=ny<m:
            y=ny

            a2[3]=a1[1]
            a2[1]=a1[4]
            a2[4]=a1[6]
            a2[6]=a1[3]
            a2[2]=a1[2]
            a2[5]=a1[5]

            a1 = process(a2,x,y)

            a2=[0,0,0,0,0,0,0]

        else:
            continue

    if cmd == 2:
        ny=y-1
        if 0<=ny<m:
            y=ny

            a2[1]=a1[3]
            a2[3]=a1[6]
            a2[6]=a1[4]
            a2[4]=a1[1]
            a2[2]=a1[2]
            a2[5]=a1[5]

            a1 = process(a2, x, y)

            a2=[0,0,0,0,0,0,0]

        else:
            continue

    if cmd == 3:
        nx = x - 1
        if 0 <= nx < n:
            x = nx

            a2[2] = a1[1]
            a2[1] = a1[5]
            a2[5] = a1[6]
            a2[6] = a1[2]
            a2[4] = a1[4]
            a2[3] = a1[3]

            a1 = process(a2, x, y)

            a2=[0,0,0,0,0,0,0]

        else:
            continue

    if cmd == 4:
        nx = x + 1
        if 0 <= nx < n:
            x = nx

            a2[2] = a1[6]
            a2[6] = a1[5]
            a2[5] = a1[1]
            a2[1] = a1[2]
            a2[4] = a1[4]
            a2[3] = a1[3]

            a1 = process(a2, x, y)

            a2=[0,0,0,0,0,0,0]

        else:
            continue