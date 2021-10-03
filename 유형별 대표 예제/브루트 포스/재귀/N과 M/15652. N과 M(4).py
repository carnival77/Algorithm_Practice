import sys
n,m = map(int,input().split())
arr=[0]*m

index=0

def recursive(index,start,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,arr))+'\n')
        return

    for i in range(start,n+1):
        arr[index] = i
        recursive(index+1,i,n,m)

recursive(0,1,n,m)