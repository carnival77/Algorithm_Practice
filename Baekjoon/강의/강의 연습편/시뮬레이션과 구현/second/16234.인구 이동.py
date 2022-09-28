from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,l,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0
for time in range(2001):
    ok=False # 인구이동 발생 여부 체크
    visit = [[False] * n for _ in range(n)] # 매일마다 국가별 방문 여부 체크
    # 격자 탐색
    for i in range(n):
        for j in range(n):
            # 만약 방문 안 했다면
            if not visit[i][j]:
                # 방문 표시
                visit[i][j]=True
                # BFS로 해당 칸에서 국경선 열 수 있는 국가 간에 연합 결성
                union=[(i,j)]
                cnt=1
                s=a[i][j]
                q=deque()
                q.append((i,j))
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and l<=abs(a[nx][ny]-a[x][y])<=r:
                            ok=True
                            q.append((nx,ny))
                            visit[nx][ny]=True
                            s+=a[nx][ny]
                            cnt+=1
                            union.append((nx,ny))
                for x,y in union:
                    a[x][y]=s//cnt
    if not ok:
        ans=time
        break
print(ans)