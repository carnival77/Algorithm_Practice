n=int(input())
p=[0]+list(map(int,input().split()))
d=[0]+[int(1e9)]*1000

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=min(d[i],d[i-j]+p[j])

# print(d)
print(d[n])