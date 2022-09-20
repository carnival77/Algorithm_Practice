# solution 1. 시간 초과
# 각 사이클을 하나씩 반시계방향으로 한칸씩 R번 회전시킨다.
# 시간초과의 이유: 2<=N,M<=300 이므로, N,M이 300이라고 하고 R을 1000이라고 했을 때, 최대 시간 (((300*300-298*298)+((298*298-296*296))+...) * 1000 ) 이 20억을 넘는다.
# 왜냐하면, 이것은 300! * 1000 보다 큰데, 54! 이후부터의 수는 무한의 수로 인간의 숫자 단위로는 셀 수 없는 수이기 때문이다.

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
#
# n,m,R = map(int,input().split())
# a=[list(map(int,input().split())) for _ in range(n)]
#
# def rotate(r,c,i):
#     x,y=i,i
#     prev=a[i][i]
#     k=0
#
#     while True:
#         if not i<=x+dx[k]<=i+r-1 or not i<=y+dy[k]<=i+c-1:
#             k=(k+1)%4
#             nx, ny = x + dx[k], y + dy[k]
#         else:
#             nx, ny = x + dx[k], y + dy[k]
#         next=a[nx][ny]
#         a[nx][ny]=prev
#         prev=next
#         x,y=nx,ny
#         if x==i and y==i:
#             break
#
# for _ in range(R):
#     r,c=n,m
#     i = 0
#     while r>0 and c>0:
#         rotate(r,c,i)
#         r-=2
#         c-=2
#         i+=1
#
# for i in range(n):
#     print(a[i])

# solution 2. 배열을 그룹 짓고 요소 rotate 후 다시 넣기
# rotate는 시간복잡도가 O(k)로, 회전횟수만큼의 시간복잡도만을 가진다.
# 그룹의 개수는 K=min(n,m)//2 다. 5x5 등으로 홀수일 경우, 가운데 1개는 돌지 않기에 회전 전과 후의 변화가 없다.
# 그룹별 요소는 윗줄, 오른쪽 줄, 아랫줄, 왼쪽 줄 순서로 큐에 담겨 회전된다.
# 수식은 위의 순서대로 a[k][j](k<=j<m-k), a[i][m-k-1](k<=i<n-k), a[n-k-1][j](k<=j<m-k), a[i][k](k<=i<n-k) 이다.
from collections import deque

n,m,R = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

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
    q.rotate(-1*R)
    for j in range(k,m-k-1):
        a[k][j] = q.popleft()
    for i in range(k,n-k-1):
        a[i][m-k-1] = q.popleft()
    for j in range(m-k-1,k,-1):
        a[n - k - 1][j] = q.popleft()
    for i in range(n-k-1,k,-1):
        a[i][k]=q.popleft()

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()

