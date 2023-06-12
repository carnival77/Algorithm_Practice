n=10
a=[list(map(int,input().split())) for _ in range(n)]
avail=[0,5,5,5,5,5]

def fill(x,y,k,num,b):
    for i in range(k):
        for j in range(k):
            b[x+i][y+j]=num
    return b

def go(z):
    global a

    if z==n*n:
        for x in range(10):
            for y in range(10):
                if a[x][y]==1:
                    return -1
        return 0

    x=z//n
    y=z%n
    if a[x][y]==0:
        return go(z+1)

    ans=-1
    for k in range(5,0,-1):
        if avail[k]<=0: continue
        if x+k-1<n and y+k-1<n:
            ok=True
            for i in range(k):
                for j in range(k):
                    if a[x+i][y+j]==0:
                        ok=False
                        break
                if not ok:
                    break
            if ok:
                a=fill(x,y,k,0,a)
                avail[k]-=1
                tmp=go(z+1)
                avail[k]+=1
                if tmp!=-1:
                    if ans==-1 or ans>tmp+1:
                        ans=tmp+1
                a=fill(x,y,k,1,a)
    return ans

print(go(0))