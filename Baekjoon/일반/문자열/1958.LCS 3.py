# d[i][j] : 수열 A의 i번째 문자까지, 수열 B의 j번째 문자까지 있을 때 LCS의 길이
import sys
input=sys.stdin.readline
a=' '+input().strip()
b=' '+input().strip()
c=' '+input().strip()
n,m,l=len(a)-1,len(b)-1,len(c)-1
d=[[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,l+1):
            # 검사하는 문자들이 같다면
            if a[i]==b[j]==c[k]:
                # metrix에서 i-1, j-1, k-1에 있는 이전까지 기록된 최장 길이 값에 +1을 해서
                # 현재 i, j, k 위치에 넣어준다.
                d[i][j][k]=d[i-1][j-1][k-1]+1
            else:
                # 일치하지 않다면, i-1 위치, j-1 위치, k-1 위치에 있는 최장 길이들 중에
                # 가장 긴 값을 가져온다.
                d[i][j][k] = max(d[i][j][k - 1], d[i][j - 1][k], d[i - 1][j][k])

print(d[n][m][l])