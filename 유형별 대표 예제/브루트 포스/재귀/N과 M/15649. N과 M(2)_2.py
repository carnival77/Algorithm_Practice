import sys
n,m = map(int,input().split())

arr=[0]*m

index=1 # 수 index
selected=0 # 선택한 수의 개수

def recursive(index,selected,n,m):
    if selected==m:
        sys.stdout.write(' '.join(map(str,arr))+'\n')
        return

    if index > n:return
    arr[selected] = index
    recursive(index+1,selected+1,n,m)
    arr[selected]=0
    recursive(index+1,selected,n,m)


recursive(index,selected,n,m)