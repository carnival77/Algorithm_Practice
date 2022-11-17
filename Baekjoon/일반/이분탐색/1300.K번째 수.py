# solution
# 이진탐색으로 작은 수의 개수가 (k-1)개인 중앙값을 찾는다.
# 그것이 오름차순 정렬된 배열 B에서의 k번째 수이다.
# NxN의 2차원 리스트는 i번째 행이 i의 배수로 구성되어 있으며, 1<=i<=N이다.
# 따라서 2차원 리스트에서의 k번째 수는 k보다 작거나 같으며, 그러므로 정답은 1~k 안에 있다.
# 따라서 start=1, end=k로 초기 설정한다.
# 또한 i번째 행에서 중앙값보다 작거나 같은 수의 개수는 min(mid//i,N)이다.
# 이것을 이용해 2차원 리스트에서 중앙값보다 작거나 같은 수의 개수를 파악한다.
# 이진탐색 조건
# i) 중앙값보다 작은 수가 k보다 적으면 start = mid+1
# ii) 중앙값보다 작은 수가 k보다 같거나 많으면 end = mid-1, ans = mid

n=int(input())
k=int(input())

start=1
end=k
ans=0

while start<=end:
    mid=(start+end)//2
    # 2차원 리스트에서 중앙값보다 작거나 같은 수의 개수를 파악
    cnt=0
    # i번째 행에서 중앙값보다 작거나 같은 수의 개수는 min(mid//i,N)이다.
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    # 중앙값보다 작은 수가 k보다 적으면 start = mid+1
    if cnt<k:
        start=mid+1
    # 중앙값보다 작은 수가 k보다 같거나 많으면 end = mid-1, ans = mid
    else:
        ans=mid
        end=mid-1

print(ans)