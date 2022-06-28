# 순열. n개 중 m개를 순서 상관하여 중복 허용 않고 뽑음

used=[False]*n
arr=[0]*m

def dfs(index,arr,nums):

    if len(arr)==m:
        return

    if index>n:
        return

    for i in range(n):
        if used[i]:
            continue
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1,arr,nums)
        used[i]=False

# 조합. n개의 수 중 m개를 순서 상관 없이 중복 허용 않고 뽑음

used=[False]*n
arr=[0]*m


def dfs(index, arr, nums,start):
    if len(arr) == m:
        return

    if index > n:
        return

    for i in range(start,n):
        if used[i]:
            continue
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1,arr,nums,i+1)
        used[i]=False

def dfs(index, arr, nums):
    if len(arr) == m:
        return

    if index > n:
        return

    dfs(index+1,arr+[nums[index]])
    dfs(index+1,arr)

# 중복 순열 문제. n개의 수 중 m개를 순서 상관하고 중복 허용하여 뽑음
def dfs(index,arr,nums):
    if len(arr) == m:
        return

    if index > n:
        return

    for i in range(n):
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1,arr,nums)
        used[i]=False

# 중복 조합 문제. n개의 수 중 m개를 순서 상관 없이 중복 허용하여 뽑음
def dfs(index, arr, nums,start):
    if len(arr) == m:
        return

    if index > n:
        return

    for i in range(start,n):
        used[i] = True
        arr[index] = nums[i]
        dfs(index + 1, arr, nums,i+1)
        used[i] = False