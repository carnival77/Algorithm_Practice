n=int(input())

a=list(map(int,input().split()))

plus,minus,mul,div = map(int,input().split())

min_ans = float('inf')
max_ans = float('-inf')

def dfs(inx,s):
    global n,a,min_ans,max_ans,plus,minus,mul,div

    if inx == n:
        max_ans = max(max_ans,s)
        min_ans = min(min_ans,s)
        return

    num = a[inx]
    if plus>0:
        plus-=1
        dfs(inx+1,s+num)
        plus+=1

    if minus>0:
        minus-=1
        dfs(inx+1,s-num)
        minus+=1

    if mul>0:
        mul-=1
        dfs(inx+1,s*num)
        mul+=1

    if div>0:
        div-=1
        dfs(inx + 1, int(s/num))
        div+=1

dfs(1,a[0])

print(max_ans)
print(min_ans)