dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

n,m,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]# 칸별 겨울에 양분 공급량
b=[[[] for _ in range(n)] for _ in range(n)]# 칸별 나무 나이 리스트

c=[[5]*n for _ in range(n)]# 칸별 잔여 양분

for _ in range(m):
    x,y,z=map(int,input().split())
    b[x-1][y-1].append(z)

for year in range(k):
    # 가을에 추가할 나이가 1인 새 나무들
    p=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lived=[]# 살아남은 나무들
            deadtrees=0# 죽은 나무들로부터의 양분을 합함.
            b[i][j].sort()# 나이가 어린 나무부터
            for tree in b[i][j]:
                if c[i][j]-tree>=0:# 나무 나이만큼의 양분 있으면 양분 -= 나무 나이 , 나무 나이 += 1
                    lived.append(tree+1)# 살아남은 나무에 해당 나무 나이 +1하여 추가
                    c[i][j]-=tree# 나무 나이만큼의 양분 있으면 양분 -= 나무 나이
                    # 가을
                    if (tree+1)%5==0:# 번식하는 나무는 나이가 5의 배수이어야 하며,
                        for k in range(8):
                            dx,dy=dir[k]
                            nx,ny=i+dx,j+dy
                            if 0<=nx<n and 0<=ny<n:
                                p[nx][ny]+=1# 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                else:
                    # 여름
                    # 양분 부족하면 나무 죽음 -> 해당 칸의 양분 += 죽은 나무 나이 // 2
                    deadtrees+=tree//2
            # 여름
            c[i][j]+=deadtrees
            # 봄
            b[i][j]=lived
            # 겨울
            c[i][j]+=a[i][j]
    # 가을
    for i in range(n):
        for j in range(n):
            for k in range(p[i][j]):
                b[i][j].append(1)
ans=0
for x in range(n):
    for y in range(n):
        for k in b[x][y]:
            if k>0:
                ans+=1
print(ans)