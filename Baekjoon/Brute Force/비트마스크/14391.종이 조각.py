# 풀이
# 1. N*M 자리 각각의 칸에 대해서 가로(0), 세로(1) 를 구분한다.
# 2. 시작 칸이 0이 아니도록 한다.
# 3. 수를 연속하는 것이 크다.
# 4. 모든 경우의 수는 2^MN 이다.
# 5. 1 <= N,M <= 4
# 6. A[i][j] : i*M + j

n,m = map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input())))
ans=0
# 1. 가로
# 1.1. n*m개 칸으로 만들어질 수 있는 모든 경우의 수 집합에 대해
for b in range(1<<m*n):
    sum=0
    # 1.2. 가로인 경우만 수를 구하고.
    for i in range(n):
        cur=0
        for j in range(m):
            k = i*m+j
            # 이번 집합 b에 대해 k가 1이 아니므로 검사 결과가 0인 경우, 가로
            if (b & (1<<k)) ==0:
                cur=cur*10 + a[i][j]
            # 1.3. 세로가 나올 경우 합한다.
            else:
                sum+=cur
                cur=0
        # 1.4. 세로-가로가 나올 경우엔 합을 구하지 않았기 때문에, 합해준다.
        sum += cur
# 2. 세로
    for j in range(m):
        cur=0
        for i in range(n):
            k = i*m + j
            if (b & (1<<k)) != 0:
                cur=cur*10 + a[i][j]
            else:
                sum+=cur
                cur=0
        sum+=cur
    ans=max(ans,sum)
print(ans)