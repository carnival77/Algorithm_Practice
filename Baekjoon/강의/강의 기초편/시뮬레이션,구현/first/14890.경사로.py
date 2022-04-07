# 피드백
# 1. 문제에 적시되지 않은 조건을 함부로 적용하지 말자. ex) 행열에 동시에 경사로 중첩되면 안된다는 등
# 2. 각 줄이 독립적이므로 한 줄씩만 함수에 넣겠다는 발상 필요
# 3. 조건 잘 읽자. ex) 경사로 길이 l 이 가변적이다.

def process(row,l):
    n = len(row)
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

n,l = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
ans=0
row=[]

for i in range(n):
    row = board[i]
    if process(row,l):
        ans +=1
for i in range(n):
    row=[]
    for j in range(n):
        row.append(board[j][i])
    if process(row,l):
        ans += 1
print(ans)
