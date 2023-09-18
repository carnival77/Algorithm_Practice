# 문제의 핵심인 아래의 3개의 조건을 파이썬 리스트의 다중조건 정렬 기능으로 만족시킨다.
# 조건들을 한 줄로 요약하면, 비어있느 칸 중에서 인접한 칸에 좋아하는 학생이 가장 많은 순,인접한 칸에 비어있는 칸이 가장 많은 순, 행 번호 오름차순, 열 번호 오름차순 이다.
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
n=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

sdict=dict()

a=[[0]*n for _ in  range(n)]

for _ in range(n ** 2):
    data = list(map(int, input().split()))
    s = data[0]
    likes = data[1:]
    sdict[s]=likes
    b = []
    for x in range(n):
        for y in range(n):
            if a[x][y] != 0:
                continue
            like_cnt = 0
            vacant_cnt=0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] in likes:
                        like_cnt += 1
                    if a[nx][ny]==0:
                        vacant_cnt+=1
            b.append((x,y,like_cnt,vacant_cnt))
    b.sort(key=lambda x:(-x[2],-x[3],x[0],x[1]))
    px,py=b[0][0],b[0][1]
    a[px][py]=s

#학생 dict를 이용해 배치된 학생들의 만족도의 합을 구한다.
ans=0
for x in range(n):
    for y in range(n):
        cnt=0
        s=a[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] in sdict[s]:
                    cnt+=1
        if cnt>=1:
            ans+=10**(cnt-1)
print(ans)