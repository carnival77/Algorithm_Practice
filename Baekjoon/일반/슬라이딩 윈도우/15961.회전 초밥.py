import sys
input=sys.stdin.readline

n,d,k,c=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))

b=[0]*(d+1)
b[c]=1
cnt=1
ans=0

for i in range(k):
    if b[a[i]]==0:
        cnt+=1
    b[a[i]]+=1
ans=max(ans,cnt)

for i in range(k,n):
    j=i-k
    if b[a[i]]==0:
        cnt+=1
    b[a[i]] += 1
    b[a[j]] -= 1
    if b[a[j]] == 0:
        cnt -= 1
    ans=max(ans,cnt)

a=a[n-k+1:]+a[:n-k+1]

b=[0]*(d+1)
b[c]=1
cnt=1

for i in range(k):
    if b[a[i]]==0:
        cnt+=1
    b[a[i]]+=1
ans=max(ans,cnt)

for i in range(k,k+(n-1-k)):
    j=i-k
    if b[a[i]]==0:
        cnt+=1
    b[a[i]] += 1
    b[a[j]] -= 1
    if b[a[j]] == 0:
        cnt -= 1
    ans=max(ans,cnt)

print(ans)