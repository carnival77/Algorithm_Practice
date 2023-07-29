import sys
from itertools import combinations
input=sys.stdin.readline

n,s=map(int,input().split())
a=list(map(int,input().split()))
ans=0

l=a[:n//2]
r=a[n//2:]

l_sum=[]
for num in range(len(l)+1):
    for comb in combinations(l,num):
        l_sum.append(sum(list(comb)))
r_sum=[]
for num in range(len(r)+1):
    for comb in combinations(r,num):
        r_sum.append(sum(list(comb)))

l_sum.sort()
r_sum.sort(reverse=True)
n,m=len(l_sum),len(r_sum)
i,j=0,0

while i<n and j<m:
    sum=l_sum[i]+r_sum[j]
    if sum==s:
        i+=1
        j+=1
        c1=1
        c2=1
        while i<n and l_sum[i]==l_sum[i-1]:
            c1+=1
            i+=1
        while j<m and r_sum[j]==r_sum[j-1]:
            c2+=1
            j+=1
        ans+=c1*c2
    elif sum<s:
        i+=1
    else:
        j+=1
if s==0:
    ans-=1
print(ans)