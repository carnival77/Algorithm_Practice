import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
l,r=0,n-1
min_val=sys.maxsize
ans=[]
# 서로 다른 두 수를 가리키는 모든 경우의 수를 탐색한다.
while l<r:
    s=a[l]+a[r]
    res=abs(s)
    # 탐색 과정 중 두 수의 합의 절댓값이 가장 작을 때, 즉 0과 가장 가까운 경우를 찾는다.
    if res<min_val:
        min_val=res
        ans=[a[l],a[r]]

    # 가리켜진 두 수의 합을 0과 비교하며 두 포인터 l과 r을 계속 이동시킨다.
    if s>0:
        r-=1
    elif s<0:
        l+=1
    else:
        print(a[l],a[r])
        sys.exit(0)

print(" ".join(map(str,ans)))