# solution.

n,x=map(int,input().split())

d=[0]*(n)
p=[0]*(n)
d[0]=1
p[0]=1

for i in range(1,n):
    d[i]=2*d[i-1]+3
    p[i]=2*p[i-1]+1

def go(n,x):
    if n==0:
        if x==0:
            return 0
        else:
            return 1
    else:
        if x==1:
            return 0
        elif 1<x<=1+d[n-1]:
            return go(n-1,x-1)
        elif x==d[n-1]+2:
            return p[n-1]+1
        elif d[n-1]+2<x<=2*d[n-1]+2:
            return p[n-1]+1+go(n-1,x-1-d[n-1]-1)
        else:
            return 2*p[n-1]+1

ans=go(n,x)
print(ans)