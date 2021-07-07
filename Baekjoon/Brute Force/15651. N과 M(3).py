import sys
n,m = map(int,input().split())
arr=[0]*m

index=0

def recursive(index,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,arr))+'\n')
        return

    for i in range(1,n+1):
        arr[index] = i
        recursive(index+1,n,m)

recursive(0,n,m)