# 풀이 시간 : 약 45분

# import sys
# sys.stdin = open("input.txt", "r")

def dfs(inx,s,kind,charges):
    global ans

    if inx>=n:
        ans=min(ans,s)
        cand.append([s,kind[:],charges[:]])
        return

    num=a[inx]
    if num==0:
        dfs(inx+1,s,kind[:],charges[:])
    else:
        # 1일
        charge = c[0] * num
        tmp_kind=kind[:]
        tmp_charges=charges[:]
        tmp_kind[inx]=1
        tmp_charges[inx]=charge
        dfs(inx+1,s+charge,tmp_kind,tmp_charges)
        # 1달
        charge = c[1]
        tmp_kind=kind[:]
        tmp_charges=charges[:]
        tmp_kind[inx]=2
        tmp_charges[inx]=charge
        dfs(inx + 1, s + charge, tmp_kind, tmp_charges)
        # 3달
        charge = c[2]
        tmp_kind=kind[:]
        tmp_charges=charges[:]
        tmp_kind[inx]=3
        tmp_charges[inx]=charge
        dfs(inx+3, s + charge, tmp_kind, tmp_charges)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    c=list(map(int,input().split()))
    a=list(map(int,input().split()))
    n=12
    ans=c[-1] # 1년
    cand=[]
    kind=[0]*12
    charges=[0]*12

    dfs(0,0,kind,charges)

    cand.sort()
    print("#"+str(t),ans)