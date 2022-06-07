n,s = map(int,input().split())
nums=list(map(int,input().split()))

answer=0

# solution 1
def dfs(index,arr,m):
    global answer
    # 정답을 찾은 경우
    if len(arr) == m:
        if sum(arr) == s:
            answer+=1
        return
    # 불가능한 경우
    if index==n:
        return

    dfs(index+1,arr+[nums[index]],m)
    dfs(index + 1, arr, m)

for i in range(1,n+1):
    dfs(0,[],i)

print(answer)

# solution 2
answer=0
def go(index,m):
    global answer
    if index==n:
        if m==s:
            answer+=1
        return
    go(index+1,m+nums[index])
    go(index+1,m)

go(0,0)
if s==0:
    answer-=1
print(answer)