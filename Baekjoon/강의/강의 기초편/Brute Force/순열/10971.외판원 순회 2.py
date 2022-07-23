from itertools import permutations

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

ans=1e9
arr=list(i for i in range(n))
for permu in permutations(arr,n):
    tmp=0
    stop=False
    for i in range(n-1):
        if a[permu[i]][permu[i+1]]!=0:
            tmp+=a[permu[i]][permu[i+1]]
        else:
            stop=True
            break
    if not stop and a[permu[-1]][permu[0]]!=0:
        tmp+=a[permu[-1]][permu[0]]
        ans=min(tmp,ans)
print(ans)