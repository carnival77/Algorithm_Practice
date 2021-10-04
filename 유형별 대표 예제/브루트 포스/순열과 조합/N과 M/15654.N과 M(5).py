# 순열 문제. 순열 : N개의 수 중 M개를 순서 상관하여 중복 허용하지 않고 뽑는다.
# 즉, 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 취급한다.
# 구하는 것 : 어떤 위치에 이전에 사용되지 않은 어떤 수가 올 것인가
# 변하는 것 : used, 위치, 수
# 변하지 않는 것 : n,m

n,m =map(int,input().split())

arr=[0]*m
used=[False]*(n)
nums =list(map(int,input().split()))
nums.sort()

# 풀이 1 : 브루트 포스 - 재귀를 통한 순열
def dfs(index):
    # 종료 조건
    if index==m:
        print(" ".join(map(str,arr)))
        return

    # 첫 번째 자리에 두 번째 이후의 수가 올 수 있는 이유 : index =0 일 때 이 for 루프가 1~(n+1)까지 돌고 있으니까
    for i in range(n):
        # 이전에 사용된 숫자라면 무시. 중복 허용 X
        if used[i]:
            continue
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1)
        used[i]=False

# dfs(0)

# 풀이 2 : permutations 라이브러리를 활용한 순열
from itertools import permutations

def permu(nums,m):
    # arr=[]
    # for i in range(1,n+1):
    #     arr.append(i)

    for i in permutations(nums,m):
        i=list(i)
        print(" ".join(map(str,i)))

permu(nums,m)