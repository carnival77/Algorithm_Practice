# solution : https://velog.io/@seung_min/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11066%EB%B2%88-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0
import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    d=[[0]*n for _ in range(n)] # dp[i][j]는 i번째 파일부터 j번째 파일을 합치는 최소값

    # 먼저 dp[i][i+1]을 구한다. 즉, 두 파일이 연속으로 되어있을 때의 합을 구하는 경우만 dp에 저장하여 초기값을 구해 놓는다.
    for i in range(n):
        for j in range(n):
            if j==i+1:
                d[i][j]=sum(a[i:j+1])

    # dp의 맨 밑에서부터 위로 올라오면서 dp를 채워 나가며, d[1][4]를 맨 마지막에 채워 넣는다.
    # dp[1][4]는 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4]와 같은 경우의 수를 가진다.
    for i in range(n-1,-1,-1):
        for j in range(n):
            if j>i and d[i][j]==0:
                d[i][j] = min([d[i][k] + d[k + 1][j] for k in range(i,j)])+sum(a[i:j+1])

    print(d[0][n-1])