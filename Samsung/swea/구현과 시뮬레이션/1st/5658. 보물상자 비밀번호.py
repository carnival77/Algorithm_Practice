# 풀이 시간 : 약 1시간 10분

#import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def process():
    global s

    lq=list(q)
    all_hex_str=[]
    for inx in range(0,n,step):
        hex_str_arr=lq[inx:inx+step]
        hex_str=''
        for str in hex_str_arr:
            hex_str+=str
        all_hex_str.append(hex_str)

    flag1=0
    for hex_str in all_hex_str:
        s.add(hex_str)

T = int(input())
for t in range(1, T + 1):
    n,K=map(int,input().split())
    q=deque(list(input()))
    step=n//4
    rotate_cnt=step-1
    s=set()
    nums=[]
    ls=[]

    process()
    q.rotate(1)

    for i in range(rotate_cnt):
        process()
        q.rotate(1)

    ls=list(s)
    ls.sort(reverse=True)

    for hex_num in ls:
        nums.append(int(hex_num,16))

    ans=nums[K-1]

    print("#" + str(t), ans)