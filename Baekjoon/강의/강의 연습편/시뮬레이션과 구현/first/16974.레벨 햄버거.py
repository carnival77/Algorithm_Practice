# solution.
# d[i] : 레벨 i 인 햄버거의 길이. d[i]=1+d[i-1]+1+d[i-1]+1=2d[i-1]+3
# p[i] : 레벨 i 인 햄버거의 패티 개수. p[i-1]+1+p[i-1]=2p[i-1]+1
# go(n,x) : 레벨 n 버거에서 아래 x장 중 패티의 개수 반환
# if n>=1:
#     x==1: 0
#     1<x<=1+d[n-1] : p[n-1]
#     x=1+d[n-1]+1 : p[n-1]+1
#     1+d[n-1]+1<x<=1+d[n-1]+1+d[n-1] : 2p[n-1]+1
#     x=1+d[n-1]+1+d[n-1]+1 : 2p[n-1]+1

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