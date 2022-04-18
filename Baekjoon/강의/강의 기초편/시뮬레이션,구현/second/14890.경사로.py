n,l=map(int,input().split())

a=[list(map(int,input().split())) for i in range(n)]

ans=0

# 조건에 맞는 지 체크
def check(row):
    global n,l
    used = [False] * n
    for i in range(1,n):
        # 인접한 칸의 높이가 다를 때만
        if row[i-1] != row[i]:
            diff = abs(row[i]-row[i-1])
            if diff!=1:
                return False

            else:
                # 2 1 1
                if row[i-1]>row[i]:
                    # l 길이는 가변적. 경사로 놓기
                    for j in range(l):
                        # 경사로 설치 X 경우
                        # 범위 벗어남
                        if i+j > n-1:
                            return False
                        # 대상 칸들의 높이 서로 다름.
                        if row[i]!=row[i+j]:
                            return False
                        # 이미 설치됨.
                        if used[i+j] == True:
                            return False
                        used[i+j]=True
                # 1 1 2
                elif row[i-1]< row[i]:
                    # l 길이는 가변적. 경사로 놓기
                    for j in range(1,l+1):
                        # 경사로 설치 X 경우
                        # 범위 벗어남
                        if i-j < 0:
                            return False
                        # 대상 칸들의 높이 서로 다름.
                        if row[i-1] != row[i - j]:
                            return False
                        # 이미 설치됨.
                        if used[i - j] == True:
                            return False
                        used[i-j] = True
    return True

# row 체크
for row in a:
    if check(row):
        ans+=1
# col 체크
for j in range(n):
    col=[]
    for i in range(n):
        col.append(a[i][j])
    if check(col):
        ans+=1
print(ans)