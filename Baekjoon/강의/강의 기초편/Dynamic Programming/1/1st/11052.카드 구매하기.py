n=int(input())

d=[0]*(n+1)
d[0]=0
a=[0] + list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=max(d[i],d[i-j]+a[j])

print(d[n])