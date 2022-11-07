# d[i][j] : 수열 A의 i번째 문자까지, 수열 B의 j번째 문자까지 있을 때 LCS의 길이
import sys
input=sys.stdin.readline
a=' '+input().strip()
b=' '+input().strip()
n,m=len(a)-1,len(b)-1
d=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i]==b[j]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i][j-1],d[i-1][j])

print(d[n][m])