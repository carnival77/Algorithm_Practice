# n세대 드래곤 커브는 n-1세대 드래곤 커브를 끝 점을 기준으로
# 시계 방향으로 90도 회전시킨 다음 n-1세대 드래곤 커브의 끝 점에 붙인 것이다.
# -> k세대의 선분들은, (k-1)세대까지의 선분들과 그 선분들을 반대 순서로,
# 반시계 방향으로 90도 회전한 방향으로 그린 선분들을 합친 것과 같다.

#  우 상 좌 하
dx=[0,-1,0,1]
dy=[1,0,-1,0]

n=int(input())
a=[[False]*101 for _ in range(101)] # 좌표 체크

# g세대까지의 선분들의 방향 리스트 반환
def curve(d,g):
    # 시작 방향부터 저장
    res=[d]
    # 이번 세대까지의 선분들의 방향 리스트 채우기
    for _ in range(g):
        # 이전 세대까지의 선분들의 방향
        ng=res[:]
        # 순서 반대로
        ng.reverse()
        # 반시계 방향 90도 회전
        for i in range(len(ng)):
            ng[i]=(ng[i]+1)%4
        # (k-1)세대까지의 선분들과 그 선분들을 반대 순서로,
        # 반시계 방향으로 90도 회전한 방향으로 그린 선분들을 합친 것
        res+=ng
    return res

for _ in range(n):
    y,x,d,g=map(int,input().split())
    # 시작점 체크
    a[x][y]=True
    dir=curve(d,g)
    # g세대까지의 선분들의 방향대로 점 (x,y) 을 옮겨가며 선분 그리기(좌표에 표시)
    for k in dir:
        x+=dx[k]
        y+=dy[k]
        a[x][y]=True
ans=0
for i in range(100):
    for j in range(100):
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
            ans+=1
print(ans)