# 시간복잡도
# : 최악의 경우 모든 강의 시간의 합의 로그 = log(2)1000000000 = 약 30 X 최악의 경우 강의의 수 = 100000
# = 약 3천만. 2초 내에 풀어야 하는데, start를 0으로 설정할 경우 시간 초과
# 따라서 start는 0이 아닌, 최대 강의 시간이고, end는 강의 시간의 합이다.

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))

start=max(a) # 블루레이의 최소 길이는 최대 강의 시간
end=sum(a) # 블루레이의 최대 길이는 강의 시간의 합
ans=0

while start<=end:
    cnt=1
    mid=(start+end)//2 # 가능한 블루레이 크기
    b=mid
    i=0
    while i<n:
        if b-a[i]>=0:
            b-=a[i]
            i+=1
        else:
            cnt+=1
            b=mid
    if cnt<=m: # 현재의 블루레이 크기로 모두 저장 가능하다면 ans에 저장한 뒤 블루레이 크기를 줄여본다
        ans=mid
        end = mid - 1
    else:
        start = mid + 1 # 모두 저장 불가능하면 블루레이 크기를 늘려본다.
print(ans)