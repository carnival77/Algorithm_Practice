#!/usr/bin/env Python
# coding=utf-8

# solution. 정점 = 원판이 놓여진 상태.  간선 = 원판 옮기기
from collections import deque
from itertools import permutations

disc=[] # 원판이 놓여져 있는 상태
for _ in range(3):
    data=input().split()
    cnt=int(data[0])
    if cnt>0:
        disc.append(data[1])
    else:
        disc.append('')
cnt=[0]*3 # 각 원판의 개수
for i in range(3):
    for ch in disc[i]:
        cnt[ord(ch)-ord('A')]+=1
d=dict()
d[tuple(disc)]=0
q=deque()
q.append(disc)
while q:
    now=q.popleft()
    for fr,to in permutations([0,1,2],2):
        if len(now[fr])==0:
            continue
        next=now[:]
        next[to]+=now[fr][-1]
        next[fr]=now[fr][:-1]
        if not tuple(next) in d:
            q.append(next)
            d[tuple(next)]=d[tuple(now)]+1
ans=['','','']
for i in range(3):
    for j in range(cnt[i]):
        ans[i]+=chr(ord('A')+i)
print(d[tuple(ans)])