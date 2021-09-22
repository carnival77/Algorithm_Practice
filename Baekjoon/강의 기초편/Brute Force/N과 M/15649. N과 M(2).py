import sys
n,m = map(int,input().split())

used = [False] * (n+1)
arr=[0]*m

index=0

def recursive(index,start,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,arr))+'\n')
        return

    for i in range(start,n+1):
        if used[i]:
            continue
        else:
            used[i] = True
            arr[index] = i
            recursive(index+1,i+1,n,m)
            used[i] = False

recursive(0,1,n,m)