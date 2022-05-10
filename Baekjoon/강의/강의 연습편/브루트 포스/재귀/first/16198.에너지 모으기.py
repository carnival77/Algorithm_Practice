n=int(input())
w=list(map(int,input().split()))

# solution 1. 재귀
def recur(w):
    n = len(w)
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n - 1):
        energy = w[i - 1] * w[i + 1]
        b = w[:i] + w[i + 1:]
        energy += recur(b)
        if ans < energy:
            ans = energy
    return ans

print(recur(w))

#solution 2. 순열.
# 순열 문제. n개의 공이 2개가 될 때까지 순서에 상관 없이, 중복 없이 공을 뽑는다.
# ans=0
# def recur2(energy):
#     global ans
#     n=len(w)
#     # 맨 앞구슬과 맨 뒤구슬만 남았을 때의 총합을 구해서 최대값 비교
#     if n==2:
#         ans=max(ans,energy)
#         return
#
#     for x in range(1,n-1):
#         # 선택한 구슬의 전, 후 값을 저장
#         result=w[x-1]*w[x+1]
#         target=w[x]
#         # 선택한 구슬 제거해주기
#         del w[x]
#         recur2(energy+result)
#         # 위에서 제거했던 구슬을 해당 위치에 다시 넣어주기
#         w.insert(x,target)
#
# recur2(0)
# print(ans)