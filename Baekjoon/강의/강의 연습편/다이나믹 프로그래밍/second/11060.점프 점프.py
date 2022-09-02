n=int(input())
a=list(map(int,input().split()))
d=[int(1e9)]*(n)
d[0]=0

for i in range(n):
    for j in range(1,a[i]+1):
        if i+j<n:
            d[i+j]=min(d[i+j],d[i]+1)
ans=-1
if d[n-1]!=int(1e9):
    ans=d[n-1]
print(ans)