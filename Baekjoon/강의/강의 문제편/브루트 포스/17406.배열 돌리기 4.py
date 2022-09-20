from itertools import permutations
from collections import deque
from copy import deepcopy

n,m,k= map(int,input().split())
a=list(list(map(int,input().split())) for _ in range(n))
ops=list(list(map(int,input().split())) for _ in range(k))
ans=int(1e9)

# 매트릭스 시계방향 90도 회전
# 배열을 그룹 짓고 요소 rotate 후 다시 넣기
# rotate는 시간복잡도가 O(k)로, 회전횟수만큼의 시간복잡도만을 가진다.
# 그룹의 개수는 K=min(n,m)//2 다. 5x5 등으로 홀수일 경우, 가운데 1개는 돌지 않기에 회전 전과 후의 변화가 없다.
# 그룹별 요소는 윗줄, 오른쪽 줄, 아랫줄, 왼쪽 줄 순서로 큐에 담겨 회전된다.
# 수식은 위의 순서대로 a[k][j](k<=j<m-k), a[i][m-k-1](k<=i<n-k), a[n-k-1][j](k<=j<m-k), a[i][k](k<=i<n-k) 이다.
def rotate_group_clock_90(a):
    n=len(a)
    m=len(a[0])

    K=min(n,m)//2

    for k in range(K):
        q=deque()
        for j in range(k,m-k-1):
            q.append(a[k][j])
        for i in range(k,n-k-1):
            q.append(a[i][m-k-1])
        for j in range(m-k-1,k,-1):
            q.append(a[n-k-1][j])
        for i in range(n-k-1,k,-1):
            q.append(a[i][k])
        q.rotate(1)
        for j in range(k, m - k - 1):
            a[k][j]=q.popleft()
        for i in range(k, n - k - 1):
            a[i][m - k - 1]=q.popleft()
        for j in range(m - k - 1, k, -1):
            a[n - k - 1][j]=q.popleft()
        for i in range(n - k - 1, k, -1):
            a[i][k]=q.popleft()

    return a

def process(sx,sy,ex,ey,b):
    n1,m1=ex-sx+1,ey-sy+1
    part=[[0]*m1 for _ in range(n1)]

    for x in range(n1):
        for y in range(m1):
            part[x][y]=b[x+sx][y+sy]

    rotated_part=rotate_group_clock_90(part)

    for x in range(n1):
        for y in range(m1):
            b[x+sx][y+sy]=rotated_part[x][y]

    return b

# 모든 연산을 순서를 바꿔가며 수행한다.
for perm in permutations(ops,k):
    b=deepcopy(a)
    for r,c,s in perm:
        sx,sy,ex,ey=r-s-1,c-s-1,r+s-1,c+s-1
        b=process(sx,sy,ex,ey,b)
    for row in b:
        ans=min(ans,sum(row))

print(ans)