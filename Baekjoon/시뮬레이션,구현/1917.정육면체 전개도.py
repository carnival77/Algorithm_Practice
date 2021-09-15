# 정육면체 전개도는 총 11가지
cubes = [
    [[1,0,0,0],
     [1,1,1,1],
     [1,0,0,0]],
    [[0,1,0,0],
     [1,1,1,1],
     [1,0,0,0]],
    [[0,0,1,0],
     [1,1,1,1],
     [1,0,0,0]],
    [[0,0,0,1],
     [1,1,1,1],
     [1,0,0,0]],
    [[0,1,0,0],
     [1,1,1,1],
     [0,1,0,0]],
    [[0,0,1,0],
     [1,1,1,1],
     [0,1,0,0]],
    [[0,0,1,1,1],
     [1,1,1,0,0]],
    [[0,0,1,1],
     [0,1,1,0],
     [1,1,0,0]],
    [[0,0,1,1],
     [1,1,1,0],
     [1,0,0,0]],
    [[1,1,0,0],
     [0,1,1,1],
     [0,1,0,0]],
    [[0,1,0,0],
     [1,1,1,0],
     [0,0,1,1]]
]

# 90도 회전
def rotate(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

# 상하, 좌우 반전
def mirror(mir,cube):
    # mir = 0 이면 상하반전
    if mir==0:
        cube = cube[::-1]
    # mir = 1 이면 좌우반전
    elif mir == 1:
        for i in range(len(cube)):
            cube[i]=cube[i][::-1]
    return cube

# 해당 큐브 범위 내에서, 보드의 숫자 구성과 일치하는 지 체크
def check(a,c,x,y):
    n=len(a)
    for i in range(len(c)):
        for j in range(len(c[0])):
            nx=x+i
            ny=y+j
            # 보드의 범위 내에서 체크
            if 0<=nx<n and 0<=ny<n:
                # 해당 큐브 범위 내 보드와 큐브의 숫자 구성이 다르면
                if a[nx][ny] != c[i][j]:
                    # False
                    return False
            else:
                return False
    return True

for _ in range(3):
    a = []
    for _ in range(6):
        a.append(list(map(int,input().split())))
    ans = False
    for cube in cubes:
        # 큐브당 상하, 좌우 반전
        for mir in range(2):
            # 큐브당 90도 회전 3번 - 360도 회전은 회전 전과 동일
            for rot in range(4):
                for x in range(6):
                    for y in range(6):
                        ans |= check(a,cube,x,y)
                cube=rotate(cube)
            cube = mirror(mir,cube)
    print("yes" if ans else "no")