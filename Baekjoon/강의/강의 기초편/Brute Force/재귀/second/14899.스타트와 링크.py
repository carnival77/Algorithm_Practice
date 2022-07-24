from itertools import combinations

n=int(input())
k=n//2
s=[list(map(int,input().split())) for _ in range(n)]
ans=1e9

def recur(index,start,link):
    global ans
    if index==n:
        if len(start)==k or len(link)==k:
            a = 0
            b = 0
            for i, j in combinations(start, 2):
                a += s[i][j] + s[j][i]
            for i, j in combinations(link, 2):
                b += s[i][j] + s[j][i]
            ans=min(ans,abs(a-b))
            return
        else:
            return
    if len(start) > k or len(link) > k:
        return

    recur(index+1,start+[index],link)
    recur(index+1,start,link+[index])

    return

recur(0,[],[])
print(ans)