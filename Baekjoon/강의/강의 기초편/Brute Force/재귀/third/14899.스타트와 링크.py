from itertools import combinations

n=int(input())
k=n//2
s=[list(map(int,input().split())) for _ in range(n)]
ans=1e9

arr=[i for i in range(n)]
for start in combinations(arr,k):
    start=list(start)
    link=[]
    for i in arr:
        if i not in start:
            link.append(i)
    a,b=0,0
    for i, j in combinations(start, 2):
        a += (s[i][j] + s[j][i])
    for i, j in combinations(link, 2):
        b += (s[i][j] + s[j][i])
    ans = min(ans, abs(a - b))
print(ans)