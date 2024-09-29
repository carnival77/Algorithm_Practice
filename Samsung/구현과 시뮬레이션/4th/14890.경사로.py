import sys

input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0

def inBoard(nx):
    if 0<=nx<n:
        return True
    return False

def check(a):

    c=[False]*n

    for i in range(n-1):
        if a[i]==a[i+1]:
            continue
        elif a[i]==a[i+1]+1:
            for j in range(m):
                if not inBoard(i+1+j) or a[i+1]!=a[i+1+j] or c[i+1+j]:
                    return 0
                c[i+1] = c[i+1+j] = True
        elif a[i]+1 == a[i + 1]:
            for j in range(m):
                if not inBoard(i-j) or a[i] != a[i - j] or c[i-j]:
                    return 0
                c[i] = c[i-j] = True
        else:
            return 0

    return 1

# 행 체크
for i in range(n):
    # res=check(a[i])
    # if res==1:
    #     ans+=res
    ans+=check(a[i])


# 열 체크
for y in range(n):
    col=[]
    for x in range(n):
        col.append(a[x][y])
    # res=check(col)
    # if res == 1:
    #     ans += res
    ans+=check(col)

print(ans)