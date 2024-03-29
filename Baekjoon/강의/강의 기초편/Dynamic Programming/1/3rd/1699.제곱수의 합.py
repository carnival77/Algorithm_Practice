# 0) 0
# 1) 1^2. 1
# 2) 1^2 + 1^2. 2
# 3) 1^2 + 1^2 + 1^2. 3
# 4) 2^2. 1
# 5) 2^2 + 1^2. 2
# 6) 2^2 + 1^2 + 1^2. 3
# 7) 2^2 + 1^2 + 1^2 + 1^2. 4
# 8) 2^2 + 2^2. 2
# 9) 3^2. 1
# 10) 3^2 + 1^2. 2
# 11) 3^2 + 1^2 + 1^2. 3

# d[i]=d[i-j^2]+1 (1<=i<=j^2)
# N을 제곱수의 합으로 나타낼 때, 마지막 수가 N의 제곱근보다 작거나 같고 1보다 같거나 큰 수들의 제곱이다.
# 이 중 최소 개수의 항으로 만들 수 있는 조합의 항의 개수를 구한다.

import math
n=int(input())

d=[0]*(n+1) # N을 제곱수의 합으로 나타낼 수 있는 최소 개수

for i in range(1,n+1):
    d[i]=i
    for j in range(1,int(math.sqrt(i))+1):
        d[i]=min(d[i],d[i-j**2]+1)
print(d[n])