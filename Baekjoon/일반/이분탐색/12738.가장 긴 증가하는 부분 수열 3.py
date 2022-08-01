# solution
# 이진탐색 활용 LIS([최장 증가 수열] LIS(Longest Increasing Subsequence))
# 리스트를 하나 생성 한 뒤 -INF(나올 수 없는 가장 작은 값)를 삽입해 줍니다.
# 이후 매번 수열을 볼때마다 벡터의 맨 뒤 원소와 현재 보고있는 수열의 원소를 비교하여
# 수열의 원소가 더 클 시 리스트에 push_back해준 뒤 LIS의 크기(답)을 1증가 시켜줍니다.
# 만약 수열의 원소가 벡터의 맨 뒤 원소보다 작거나 같을 경우 리스트에서 lower_bound를 이용하여
# 최적의 자리를 찾은 뒤 그 자리의 값을 해당 수열의 원소로 교체해 버립니다.

# 설명 링크 : https://jason9319.tistory.com/113

from bisect import bisect_left
import sys

n=int(input())
a=list(map(int,input().split()))
b=[-sys.maxsize]

for i in a:
    if i>b[-1]:
        b.append(i)
    else:
        b[bisect_left(b,i)]=i

print(len(b)-1)