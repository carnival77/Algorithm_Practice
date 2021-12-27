import sys

# solution 1. template 2 사용
# def dfs(index,n,s,ans):
#
#     if len(ans) == 6:
#         print(" ".join(map(str,ans)))
#         return
#
#     if index >= n:
#         return
#
#     dfs(index+1,n,s,ans+[s[index]])
#     dfs(index+1,n,s,ans)

# solution 2. template 1 사용
def dfs(index,n,s,ans,start,used):

    if index == 6:
        print(" ".join(map(str, ans)))
        return

    for i in range(start,n):
        if used[i]:
            continue
        used[i]=True
        ans[index]=s[i]
        dfs(index+1,n,s,ans,i+1,used)
        used[i]=False


while True:
    data = list(map(int,input().split()))

    k=data[0]

    if k==0:
        sys.exit(0)

    s=data[1:]

    used=[False]*k
    ans=[0]*6

    dfs(0,k,s,ans,0,used)

    print()