import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())

a=[]

for _ in range(n):
    a.append(list(map(int,input().split())))

# 그룹의 개수는 n//2 과 m//2 중 최솟값
groupn = min(n//2,m//2)

groups = []
# index=0

# 맨 마지막 수부터 첫 번째 수까지 거꾸로 넣는다.
for k in range(groupn):
    group=[]
    for j in range(k,m-k):
        group.append(a[k][j])
    for i in range(k+1,n-k-1):
        group.append(a[i][m-k-1])
    for j in range(m-k-1,k,-1):
        group.append(a[n-k-1][j])
    for i in range(n-k-1,k,-1):
        group.append(a[i][k])
    groups.append(group)

for k in range(groupn):
    group = groups[k]
    l = len(group)
    # k번째 그룹의 index는, 그룹의 총 개수인 l 보다 많이 회전하면 그것을 l로 나눈 나머지와 같이 회전한다.
    index = (r%l)
    # 총 l 개를 4개의 사이드에서 위에서 넣은 순서에 index를 더한 순서로 재배열한다.
    for j in range(k,m-k):
        a[k][j] = group[index]
        index = (index+1)%l
    for i in range(k+1,n-k-1):
        a[i][m-k-1] = group[index]
        index = (index + 1) % l
    for j in range(m-k-1,k,-1):
        a[n-k-1][j] = group[index]
        index = (index + 1) % l
    # 마지막 사이드를 채울 때, index를 l로 나눈 나머지가 0부터 시작되며, group의 첫 번째 숫자부터 삽입되어 완성된다.
    for i in range(n-k-1,k,-1):
        a[i][k] = group[index]
        index = (index + 1) % l

for row in a:
    print(*row,sep=' ')