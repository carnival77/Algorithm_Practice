import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))
d=deque() # 덱의 첫 번째 값이 [최솟값 인덱스, 최솟값]이 되도록 유지.

for i,num in enumerate(a):
    while d and d[-1][1]>num:   # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
        d.pop()
    d.append([i,num])           # 덱의 마지막 위치에 현재 값 저장
    if d[0][0]<i-k+1:           # 덱의 첫 번째 위치에서부터 L의 범위를 벗어난 값을 덱에서 제거
        d.popleft()
    print(d[0][1],end=' ')      # 덱의 첫 번째 데이터 출력