from itertools import permutations

n=int(input())
a=list(map(int,input().split()))
ans=0

for b in permutations(a,n):
    tmp=0
    for i in range(n-1):
        tmp+=abs(b[i]-b[i+1])
    ans=max(ans,tmp)

print(ans)