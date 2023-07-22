import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

rs=list(map(int,input().split()))

def five(a,n,m):
    b=[[0]*m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            b[i][m//2+j]=a[i][j]
            b[n//2+i][m//2+j]=a[i][m//2+j]
            b[n//2+i][j]=a[n//2+i][m//2+j]
            b[i][j]=a[n//2+i][j]

    return b

def six(a,n,m):
    b=[[0]*m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            b[n//2+i][j]=a[i][j]
            b[n//2+i][m//2+j]=a[n//2+i][j]
            b[i][m//2+j]=a[n//2+i][m//2+j]
            b[i][j]=a[i][m//2+j]

    return b

for inx in range(r):
    n=len(a)
    m=len(a[0])
    cmd=rs[inx]
    if cmd==1:
        a=a[::-1]
    elif cmd==2:
        for i in range(n):
            a[i]=a[i][::-1]
    elif cmd==3:
        a=list(map(list,zip(*a[::-1])))
    elif cmd==4:
        a=list(map(list,zip(*a)))[::-1]
    elif cmd==5:
        a=five(a,n,m)
    else:
        a=six(a,n,m)

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end = ' ')
    print()
