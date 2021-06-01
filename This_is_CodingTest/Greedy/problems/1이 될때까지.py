
if __name__ == '__main__':

    n,m = map(int,input().split())

    cnt=0

    # while n!=1:
    #     if n%m == 0:
    #         n/=m
    #         cnt+=1
    #     else:
    #         n-=1
    #         cnt += 1

    while True:
        target = (n//m)*m
        cnt+=(n-target)
        n=target
        if n<m:
            break
        cnt+=1
        n//=m

    cnt+=(n-1)
    print(cnt)
#