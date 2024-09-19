# 풀이 시간 : 약 1시간 50분

# import sys
# sys.stdin = open("input.txt", "r")

from itertools import combinations

def copyBoard(a):
    return [row[:] for row in a]

def inspect(ta,tb):

    # 복사된 맵에 A,B 층 변경을 적용하고
    b=copyBoard(a)
    for layer in ta:
        b[layer]=[0]*m
    for layer in tb:
        b[layer]=[1]*m

    # 전체 열을 순차 탐색하며 합격 기준 K를 만족하는지 확인
    totchk=True
    for y in range(m):
        # 이번 열은 만족하는지 확인
        ychk=False
        for x in range(n-K+1):
            # 이번 위치에서 아래로 K개만큼 탐색하며 K개가 서로 동일하여 합격 기준 K 만족하는지 확인
            Kchk=True
            for k in range(K):
                if b[x][y]!=b[x+k][y]:
                    # 하나라도 다른 게 나오면 실패
                    Kchk = False
                    break
            # 합격 기준 통과했으면 이번 열은 성공
            if Kchk:
                ychk=True
                break
        # 이번 열이 실패했으면 전체 열도 실패
        if not ychk:
            totchk=False
            return totchk

    return totchk

def process():

    arr=[i for i in range(n)]
    # arr 배열 중 cnt개를 선택하는 조합 comb 중에서
    for comb in combinations(arr,cnt):
        for num in range(cnt+1):
            # comb 중 num(0~cnt)개를 선택하는 조합 comb2를 구하고
            for comb2 in combinations(comb,num):
                ta=list(comb2) # comb2에 속한 층은 A로 변경
                tb=[]
                for layer in comb:
                    if layer not in ta:
                        tb.append(layer) # comb2에 속하지 않은 층은 B로 변경
                # 합격 기준 통과하는지 검사
                ok=inspect(ta,tb)
                if ok:
                    return True

    return False

T = int(input())
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