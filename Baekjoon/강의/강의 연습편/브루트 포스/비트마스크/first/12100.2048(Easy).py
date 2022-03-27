LIMIT = 5

# 비트 연산 사용하여 정수 k를 (2진법으로 나타난 후) 4진법으로 변환하여 반환
def gen(k):
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a

# 보드 a를 그 방향(dirs)으로 이동 시켜서, 최댓값을 반환한다.
def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    # 0: down, 1: up, 2: left, 3: right
    for dir in dirs:
        ok = False
        merged = [[False] * n for _ in range(n)]

        while True:
            ok = False
            if dir == 0:
                for i in range(n - 2, -1, -1):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i + 1][j] == 0:
                            d[i + 1][j] = d[i][j]
                            merged[i + 1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i + 1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i + 1][j]:
                                d[i + 1][j] *= 2
                                merged[i + 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 1:
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i - 1][j] == 0:
                            d[i - 1][j] = d[i][j]
                            merged[i - 1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i - 1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i - 1][j]:
                                d[i - 1][j] *= 2
                                merged[i - 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 2:
                for j in range(1, n):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j - 1] == 0:
                            d[i][j - 1] = d[i][j]
                            merged[i][j - 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j - 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j - 1]:
                                d[i][j - 1] *= 2
                                merged[i][j - 1] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 3:
                for j in range(n - 2, -1, -1):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j + 1] == 0:
                            d[i][j + 1] = d[i][j]
                            merged[i][j + 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j + 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j + 1]:
                                d[i][j + 1] *= 2
                                merged[i][j + 1] = True
                                d[i][j] = 0
                                ok = True
            if not ok:
                break

    ans = max([max(row) for row in d])
    return ans


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 모든 이동 방법을 만든다. 여기서 k는 정수(비트마스크)이다.
for k in range(1 << (LIMIT * 2)):
    # gen 함수를 통해, 정수 k를 0,1,2,3 으로 이뤄진 4진법 수로 바꾼다. 0,1,2,3은 위,아래,오른쪽,왼쪽 4가지 방향을 가리킨다.
    # 즉, dirs 는 10번 안에 가능한 모든 4가지 방향들의 집합이다.
    dirs = gen(k)
    cur = check(a, dirs)
    if ans < cur:
        ans = cur
print(ans)