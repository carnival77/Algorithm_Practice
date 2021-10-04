# 조합 문제. 조합 : N개의 수 중 M개를 순서 상관 하고 중복 허용하지 않고 뽑는다.
# 추가 조건 : 오름차순
# 구하는 것 : 어떤 위치에 이전에 사용되지 않은 어떤 수가 올 것인가
# selected : 선택한 수 개수 및 위치
# index : 오름차순 수

n,m =map(int,input().split())

arr=[0]*m
used=[False]*(n)
nums =list(map(int,input().split()))
nums.sort()

def dfs(index,selected):
    # 종료 조건
    if selected==m:
        print(" ".join(map(str,arr)))
        return

    if index >=n:
        return

    # 선택 O
    arr[selected]=nums[index]
    dfs(index+1,selected+1)
    # 선택 X
    arr[selected]=0
    dfs(index+1,selected)

dfs(0,0)