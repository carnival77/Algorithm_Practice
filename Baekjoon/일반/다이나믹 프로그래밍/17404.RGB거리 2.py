#for문을 3번을 돌며 첫번째 for문에서는 첫 번째 집을 R로 칠했을 때의 최소비용을 dp테이블에 저장하고,
# 두번째는 첫 번째집을 G로 칠했을때의 최소비용 dp 테이블, 3번째는 첫 번째집을 B로 칠했을 때의 최소비용 dp테이블을 만드는 것입니다.
# 그리고 각 for문의 끝에서 dp테이블 중에 첫 번째 집과 마지막 집의 색이 다를 때만 비용을 보며, 최솟값을 갱신해 나갑니다.

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
INF=int(1e9)
ans=INF

for i in range(3):
    d=[[INF]*3 for _ in range(n)]# dp가 각 R, G, B로 시작했을 때
    d[0][i]=a[0][i]# 처음 집 색칠
    for j in range(1,n):# 2번째 집부터 R, G, B로 색칠했을 때 최소값 갱신
        d[j][0] = min(d[j-1][1],d[j-1][2])+a[j][0]
        d[j][1] = min(d[j-1][0],d[j-1][2])+a[j][1]
        d[j][2] = min(d[j-1][0],d[j-1][1])+a[j][2]
    for k in range(3):
        if i!=k:# 첫번째 집과 N번째 집이 다른 경우만 선택
            ans=min(ans,d[-1][k])

print(ans)

