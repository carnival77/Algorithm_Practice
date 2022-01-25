 # 조합 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관하며 사용. 즉, 순서가 달라도 같은 요소로 구성되어 있으면 같은 집합
# 순열 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합
# 중복 순열 문제. N개 중 M개를 선택하여 중복 허용 O, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합

1. board = [list(input()) for _ in range(n)]
: 정수 배열을 행렬로 입력
CCP
CCP
PPC

[['C', 'C', 'P'], ['C', 'C', 'P'], ['P', 'P', 'C']]

% 주의! input = sys.stdin.readline 으로 설정하면, 엔터(/n)도 같이 입력되니 주의
ex ) [['C', 'C', 'P', '\n'], ['C', 'C', 'P', '\n'], ['P', 'P', 'C', '\n']]

# 시계 방향 회전
temp = a[i][7]
for j in range(7, 0, -1):
    a[i][j] = a[i][j - 1]
a[i][0] = temp

# 반시계 방향 회전
temp = a[i][0]
for j in range(7):
    a[i][j] = a[i][j + 1]
a[i][7] = temp

>>> a = ['a', 'b', 'c', 'd', 'e']
>>> a[  : -1 ]
['a', 'b', 'c', 'd']

1. a[N:M]
a[N] <= x < a[M]
a[N] <= x <= a[M-1]
N을 포함한 인덱스 부터 M을 포함하지 않는 인덱스 까지를 자르는 기능을 합니다.

2. a[:M]
a[0] <= x < a[M]
a[0] <= x <= a[M-1]

3. a[N:]
a[N] <= x < a[len(a)]
a[N] <= x <= a[len(a) - 1]
len(a)는 리스트의 길이를 말합니다.

4. a[:] 이처럼 양쪽을 비워서 슬라이싱을 한다는 것은 리스트 전체를 복사하는것과 동일합니다.
a[0] <= x < a[len(a)]
a[0] <= x <= a[len(a) - 1]

# 우측으로 요소 한 칸씩 이동.
a = a[-1:] + a[:-1]
c = c[-1:] + c[:-1]

# reverse
temp = temp[::-1]

# 줄바꿈 없이 출력
print("안녕하세요", end=' ')

- ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.

- '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

# 배열 90도 회전
def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result


# 상하 반전
n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0] * m for _ in range(n)]

# 1. 반복문
for i in range(n):
    temp[i] = arr[n - 1 - i]

# 2. 문자열 슬라이싱
arr = arr[::-1]

# 좌우 반전
n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0] * m for _ in range(n)]

# 1. 반복문
for i in range(n):
    for j in range(m):
        temp[i][j] = arr[i][m - 1 - j]

# 2. 문자열 슬라이싱
for i in range(n):
    arr[i] = arr[i][::-1]

# 무한의 수 표현
INF = float('inf')
