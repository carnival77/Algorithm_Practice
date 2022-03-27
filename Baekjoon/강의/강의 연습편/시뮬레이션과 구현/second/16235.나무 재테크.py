# 3차원 배열을 trees=[[[] for _ in range(n)] for _ in range(n)] 로 선언
#
n,m,k = map(int,input().split())

# 칸별 겨울에 양분 공급량
a=[]

for _ in range(n):
    a.append(list(map(int,input().split())))

# 칸별 나무 나이 리스트
trees=[[[] for _ in range(n)] for _ in range(n)]
# 칸별 잔여 양분
food = [[5] * n for _ in range(n)]

for _ in range(m):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

ans=0
for time in range(k):
    # 가을에 추가할 나이가 1인 새 나무들
    p = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            lived=[] # 살아남은 나무들
            # 봄
            # 나이가 어린 나무부터
            trees[i][j].sort()
            # 죽은 나무들로부터의 양분을 합함.
            deadtree=0
            # 나무 나이만큼의 양분 있으면 양분 -= 나무 나이 , 나무 나이 += 1.
            for tree in trees[i][j]:
                if tree <= food[i][j]:
                    # 나무 나이만큼의 양분 있으면 양분 -= 나무 나이
                    food[i][j] -= tree
                    # 살아남은 나무에 해당 나무 나이 +1하여 추가
                    lived.append(tree+1)
                    # 가을
                    # 번식하는 나무는 나이가 5의 배수이어야 하며,
                    if (tree+1) % 5 == 0:
                        for dir in range(8):
                            nx, ny = i + dx[dir], j + dy[dir]
                            # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                            if 0 <= nx < n and 0 <= ny < n:
                                # 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                                p[nx][ny] += 1
                # 양분 부족하면 나무 죽음 -> 해당 칸의 양분 += 죽은 나무 나이 // 2
                else:
                    deadtree += tree//2
            trees[i][j] =lived
            food[i][j] += deadtree
            food[i][j] += a[i][j] # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
    # 가을에 추가할 나이가 1인 새 나무들 추가
    for i in range(n):
        for j in range(n):
            for k in range(p[i][j]):
                trees[i][j].append(1)

for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)