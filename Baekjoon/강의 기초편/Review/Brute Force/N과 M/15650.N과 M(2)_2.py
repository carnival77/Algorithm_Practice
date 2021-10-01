# 구하는 것 : 어떤 위치에 이전에 사용되지 않은 어떤 수가 올 것인가
# selected : 선택한 수 개수 및 위치
# index : 오름차순 수

n,m =map(int,input().split())

arr=[0]*m

def dfs(index,selected):
    # 종료 조건
    if selected==m:
        print(" ".join(map(str,arr)))
        return
    if index>n:
        return

    # 선택 O
    arr[selected] = index
    dfs(index+1,selected+1)
    # 선택 X
    arr[selected]=0
    dfs(index+1,selected)


dfs(1,0)