from itertools import permutations

n = int(input())
k=int(input())

nums=[]

for i in range(n):
    nums.append(int(input()))

# solution 1 : dfs 활용
arr=[0] * k
used=[False] * n
result=set()

def dfs(index):
    # global ans
    if index==k:
        result.add("".join(map(str,arr)))
        return
    if index>k:
        return

    for i in range(n):
        if used[i]:
            continue
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1)
        used[i]=False

dfs(0)

result2=set()

# solution 2 : permutation 활용
for i in permutations(nums,k):
    result2.add("".join(map(str,i)))

ans=len(result)

print(ans)