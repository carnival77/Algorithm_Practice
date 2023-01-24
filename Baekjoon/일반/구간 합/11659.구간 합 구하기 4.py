n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))

s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+a[i]

for _ in range(m):
    i,j=map(int,input().split())
    res=s[j]-s[i-1]
    print(res)