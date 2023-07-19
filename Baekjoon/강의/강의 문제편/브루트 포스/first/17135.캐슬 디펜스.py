from itertools import combinations
import copy

n,m,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0
where=[]
for i in range(m):
    where.append((n,i))

for comb in combinations(where,3):
    b=copy.deepcopy(a)
    res=0
    for turn in range(1,n+1):
        ok=True
        for i in range(n):
            for j in range(m):
                if b[i][j]==1:
                    ok=False
        if ok:
            break
        # 공격
        killed=[None]*3
        for inx,archer in enumerate(comb):
            x,y=archer
            cand=[]
            for i in range(n):
                for j in range(m):
                    dist=abs(i-x)+abs(j-y)
                    if b[i][j]==1 and dist<=d:
                        cand.append([dist,i,j])
            if len(cand) > 0:
                cand.sort(key=lambda x:(x[0],x[2]))
                killed[inx]=cand[0][1:]
        for k in killed:
            if k is not None:
                i,j=k
                if b[i][j]==1:
                    b[i][j]=0
                    res+=1
        # 적 이동
        for i in range(n-1,-1,-1):
            for j in range(m):
                if i==0:
                    b[i][j]=0
                else:
                    b[i][j]=b[i-1][j]
    ans=max(ans,res)
print(ans)