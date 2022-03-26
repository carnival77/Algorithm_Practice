# 중복조합 문제. 조합 : N개의 수 중 M개를 순서 상관없이 중복 허용하여 뽑는다.
# 추가 조건 : 오름차순
# 구하는 것 : 어떤 위치에 이전에 사용되지 않은 어떤 수가 올 것인가
# 변하는 것 : used, 위치, 수
# 변하지 않는 것 : n,m

import sys

# 풀이 1 : 브루트 포스 - 재귀를 통한 중복조합
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = [0]*m
index=0

def recursive(index,start,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,result))+'\n')
        return

    for i in range(start,n):
        result[index] = arr[i]
        recursive(index+1,i,n,m)

# recursive(0,0,n,m)

# 풀이 2 : combinations_with_replacement 라이브러리를 활용한 중복조합
from itertools import combinations_with_replacement

def combirepl(arr,m):
    # arr=[]
    # for i in range(1,n+1):
    #     arr.append(i)

    for i in combinations_with_replacement(arr,m):
        i=list(i)
        print(" ".join(map(str,i)))

combirepl(arr,m)