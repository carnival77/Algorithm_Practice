# 행렬 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n =len(a) # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    n = len(new_lock)//3
    for i in range(n):
        for j in range(n):
            if new_lock[n+i][n+j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 기존 크기의 3배로 변환
    new_lock = [[0] * (3*n) for _ in range(3*n)]
    # new lock 의 중앙에 기존 자물쇠 삽입
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 회전하기
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        # 탐색 범위 : 0 ~ (2n + m)
        for x in range(2*n):
            for y in range(2*n):
                # key 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                else:
                    # key 도로 빼기
                    for i in range(m):
                        for j in range(m):
                            new_lock[x + i][y + j] -= key[i][j]
    return False

