# [풀이 시간]
# 1회 : 약 35분

t=int(input())
answer=[[] for _ in range(t)]

def check(s):
    tmp=''
    for e in s:
        if e!=' ':
            tmp+=e
    if eval(tmp)==0:
        return True
    return False

def dfs(inx,s):
    global answer

    if inx>=n:
        return

    s+=arr[inx]

    if inx==n-1:
        if check(s):
            answer[round].append(s)

    dfs(inx+1,s+'+')
    dfs(inx+1,s+'-')
    dfs(inx+1,s+' ')

for round in range(t):
    n=int(input())
    arr=[str(i) for i in range(1,n+1)]

    dfs(0,'')
    answer[round].sort()

for inx,ans in enumerate(answer):
    for res in ans:
        print(res)
    if inx<t-1:
        print()