# 풀이 시간 : 약 1시간 30분

# import sys
# sys.stdin = open("input.txt", "r")

from itertools import combinations

def copyBoard(a):
    return [row[:] for row in a]

def inspect(ta,tb):

    b=copyBoard(a)
    for layer in ta:
        b[layer]=[0]*m
    for layer in tb:
        b[layer]=[1]*m

    totchk=True
    for y in range(m):
        ychk=False
        for x in range(n-K+1):
            Kchk=True
            for k in range(K):
                if b[x][y]!=b[x+k][y]:
                    Kchk = False
                    break
            if Kchk:
                ychk=True
                break
        if not ychk:
            totchk=False
            return totchk

    return totchk

def process():

    arr=[i for i in range(n)]
    for comb in combinations(arr,cnt):
        for num in range(cnt+1):
            for comb2 in combinations(comb,num):
                ta=list(comb2)
                tb=[]
                for layer in comb:
                    if layer not in ta:
                        tb.append(layer)
                ok=inspect(ta,tb)
                if ok:
                    return True

    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    n,m,K=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]
    cnt=0

    while True:
        ok=process()
        if ok:
            break
        cnt+=1

    print("#" + str(t), cnt)