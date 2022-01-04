N,S = map(int,input().split())

nums=list(map(int,input().split()))

n=len(nums)

answer=0

def dfs(index,sum):
    global answer
    if n==index:
        if sum==S:
            answer+=1
        return

    dfs(index+1,sum+nums[index])
    dfs(index+1,sum)

dfs(0,0)

# def dfs(index,arr):
#     global answer
#     if n==index:
#         if S==sum(arr):
#             answer+=1
#             print(arr)
#         return
#
#     dfs(index+1,arr+[nums[index]])
#     dfs(index+1,arr)

# dfs(0,[])

if S==0:
    answer-=1

print(answer)