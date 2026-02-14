def solution(info, n, m):
    ans = 0

    arr=info
    arr.sort(key=lambda x:(x[1]/x[0],-x[0],x[1]))
    a,b=0,0

    print(arr)

    for x,y in arr:
        if b+y<m:
            b+=y
        else:
            if a+x<n:
                a+=x
            else:
                return -1
    ans=a
    return ans

# info=[[1, 2], [2, 3], [2, 1]]
# info=[[1, 2], [2, 3], [2, 1]]
# info=[[3, 3], [3, 3]]
# info=[[3, 3], [3, 3]]
info = [[1,11],[2,3],[4,6]]
# n=4
# n=1
# n=7
# n=6
n=5
# m=4
# m=7
# m=1
# m=1
m=12
print(solution(info,n,m))