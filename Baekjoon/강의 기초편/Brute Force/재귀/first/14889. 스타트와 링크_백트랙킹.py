# 백트랙킹 = 브루트 포스를 진행하다가 더 이상 함수 호출이 의미 없을 경우, 이런 경우를 제외하고 진행하는 것
# 가능한 종료 조건을 모두 고려하여 구현
# 가능한 경우의 수 : first, second 그룹에 사람을 넣는 경우의 수
# 넣고난 다음, 각 능력치 고르기 위해 탐색 범위를 n//2 까지로 설정하여 i==j인 경우 continue, 그 외의 경우 능력치의 합과 격차를 구한다.
# ans == -1인 경우와 t1, t2가 -1 이상의 수가 나왔을 경우 최댓값을 갱신한다.

n=int(input())

s=[]

for i in range(n):
    s.append(list(map(int,input().split())))

first=[]
second=[]

def recur(index, first, second):
    if index == n:
        if len(first) != n // 2: return -1
        if len(second) != n // 2: return -1

        t1 = 0
        t2 = 0

        for i in range(n // 2):
            for j in range(n // 2):
                if i == j: continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    if len(first) > n//2: return -1
    if len(second) > n//2 : return -1
    ans = -1
    t1 = recur(index+1, first+[index],second)
    if ans==-1 or (t1 != -1 and ans>t1):
        ans = t1
    t2 = recur(index+1, first, second+[index])
    if ans==-1 or (t2 != -1 and ans>t2):
        ans = t2
    return ans

print(recur(0,first,second))