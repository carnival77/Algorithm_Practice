# 조합 문제. 조합 : N개의 수 중 M개를 순서 상관 하고 중복 허용하지 않고 뽑는다.
# 추가 조건 : 오름차순
# 구하는 것 : 어떤 위치에 이전에 사용되지 않은 어떤 수가 올 것인가
# 변하는 것 : used, 위치, 수
# 변하지 않는 것 : n,m

n,m =map(int,input().split())

arr=[0]*m
used=[False]*(n+1)

def dfs(index,start):
    # 종료 조건
    if index==m:
        print(" ".join(map(str,arr)))
        return

    # 첫 번째 자리에 두 번째 이후의 수가 올 수 있는 이유 : index =0 일 때 이 for 루프가 1~(n+1)까지 돌고 있으니까
    for num in range(start,n+1):
        # 이전에 사용된 숫자라면 무시
        if used[num]:
            continue
        used[num]=True
        arr[index]=num
        dfs(index+1,num+1)
        used[num]=False

dfs(0,1)