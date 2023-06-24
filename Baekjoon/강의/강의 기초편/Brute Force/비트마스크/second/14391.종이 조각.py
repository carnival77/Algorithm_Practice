import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,list(input().strip()))) for _ in range(n)]
ans=0
pos=[]
for i in range(n):
    for j in range(m):
        pos.append([i,j])

for num in range(n*m+1):
    for comb in combinations(pos,num):
        res=0
        b = [[1] * m for _ in range(n)] # 0이면 가로, 1이면 세로
        for x,y in list(comb):
            b[x][y]=0
        # 가로
        for x in range(n):
            cur = 0
            for y in range(m):
                if b[x][y]==0:
                    if cur==0:
                        cur=a[x][y]
                    else:
                        cur=cur*10+a[x][y]
                else:
                    res+=cur
                    cur=0
            res+=cur
        # 세로
        for y in range(m):
            cur = 0
            for x in range(n):
                if b[x][y] == 1:
                    if cur == 0:
                        cur = a[x][y]
                    else:
                        cur = cur * 10 + a[x][y]
                else:
                    res += cur
                    cur = 0
            res += cur
        ans=max(ans,res)
print(ans)