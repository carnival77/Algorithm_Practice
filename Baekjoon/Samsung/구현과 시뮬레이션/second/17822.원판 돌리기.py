from collections import deque
import sys
input = sys.stdin.readline

n,m,t=map(int,input().split())
circle=[deque()]*n
ans=0

for i in range(n):
    data=list(map(int,input().split()))
    circle[i]=deque(data)

def get_direction(d):
    if d==0: return 1
    else: return -1

for _ in range(t):
    x,d,k=map(int,input().split())
    #1
    for i in range(n):
        if (i+1)%x==0:
            circle[i].rotate(get_direction(d)*k)
    #2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
    ok=True # 인접한 수가 없으면 True. 있으면 False
    #2-1. 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
    zero=[]
    for i in range(n):
        for j in range(m):
            if circle[i][j]==circle[i][(j+1)%m] and circle[i][j]!=0 and circle[i][(j+1)%m]!=0:
                zero.append((i,j))
                zero.append((i,(j+1)%m))
                ok=False
            if i<n-1:
                if circle[i][j]==circle[i+1][j] and circle[i][j]!=0 and circle[i+1][j]!=0:
                    zero.append((i,j))
                    zero.append((i+1,j))
                    ok=False
    for r,c in zero:
        circle[r][c]=0
    #2-2. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    if ok:
        s,cnt=0,0
        for i in range(n):
            for j in range(m):
                if circle[i][j]!=0:
                    s+=circle[i][j]
                    cnt+=1
        if cnt==0: continue
        avg=s/cnt
        for i in range(n):
            for j in range(m):
                if circle[i][j]!=0:
                    if circle[i][j]<avg:
                        circle[i][j]+=1
                    elif circle[i][j]>avg:
                        circle[i][j]-=1
for i in range(n):
    for j in range(m):
        ans+=circle[i][j]
print(ans)