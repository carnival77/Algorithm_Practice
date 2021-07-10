import sys
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = [0]*m
index=0

def recursive(index,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,result))+'\n')
        return

    for i in range(n):
        result[index] = arr[i]
        recursive(index+1,n,m)

recursive(0,n,m)