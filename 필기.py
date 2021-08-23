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

#슬라이스, 마지막 요소는 포함 안 한다.
a[1:4]
4-1 index 까지만 가지고 온다는 거군요.

1. 슬라이싱은 리스트 a의 a[N:M] 이라고 한다면 아래의 식을 만족합니다.
a[N] <= x < a[M]
a[N] <= x <= a[M-1]
N을 포함한 인덱스 부터 M을 포함하지 않는 인덱스 까지를 자르는 기능을 합니다.

2. 슬라이싱을 할때 맨 앞을 비워둔다면 a[:M] 이렇게 표현할 수 있으며 이는 아래의 식을 말합니다.
a[0] <= x < a[M]
a[0] <= x <= a[M-1]

3. 뒤를 비워두는 a[N:] 이런 식이라면
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