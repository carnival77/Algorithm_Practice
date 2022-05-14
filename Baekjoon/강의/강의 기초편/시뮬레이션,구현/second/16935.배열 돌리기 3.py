n,m,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
cmds=list(map(int,input().split()))

def process(cmd):
    global a
    n=len(a)
    m=len(a[0])
    b=[[0]*m for _ in range(n)]

    if cmd==1:
        for i in range(n):
            for j in range(m):
                b[n-1-i][j]=a[i][j]

    elif cmd==2:
        for i in range(n):
            for j in range(m):
                b[i][m-1-j]=a[i][j]

    elif cmd==3:
        b = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                b[j][n-1-i]=a[i][j]

    elif cmd==4:
        b = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                b[m-1-j][i]=a[i][j]

    elif cmd==5:
        for i in range(n):
            for j in range(m):
                if 0<=i<n//2 and 0<=j<m//2:
                    b[i][j+m//2]=a[i][j]
                elif 0<=i<n//2 and m//2<=j<m:
                    b[i+n//2][j]=a[i][j]
                elif n//2<=i<n and m//2<=j<m:
                    b[i][j-m//2]=a[i][j]
                else:
                    b[i-n//2][j]=a[i][j]

    else:
        for i in range(n):
            for j in range(m):
                if 0<=i<n//2 and 0<=j<m//2:
                    b[i+n//2][j]=a[i][j]
                elif n//2<=i<n and 0<=j<m//2:
                    b[i][j+m//2]=a[i][j]
                elif n//2<=i<n and m//2<=j<m:
                    b[i-n//2][j]=a[i][j]
                else:
                    b[i][j-m//2]=a[i][j]
    a=b

for cmd in cmds:
    process(cmd)

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end = ' ')
    print()
