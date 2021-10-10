# 참고 : https://pearlluck.tistory.com/625


from copy import deepcopy

import sys

input =sys.stdin.readline

n,x = map(int,input().split())

a=list(map(int,input().split()))

if max(a)==0:
    print('SAD')
    sys.exit(0)

# 슬라이딩 윈도우 초기값 설정
max_value,value = sum(a[:x]),sum(a[:x])
max_cnt = 1

#슬라이딩 윈도우 진행
for i in range(x,n):
    # 슬라이딩 윈도우 오른쪽 +
    value += a[i]
    # 슬라이딩 윈도우 왼쪽 -
    value -= a[i-x]

    # max_value, max_cnt  업데이트
    if value > max_value:
        max_value=value
        max_cnt=1
    elif value == max_value:
        max_cnt+=1

print(max_value)
print(max_cnt)