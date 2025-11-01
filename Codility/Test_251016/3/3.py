# def solution(A, B):
#     ans=0
#     c=[]
#     z=0
#     for x,y in zip(A,B):
#         if x==y:
#             c.append(x)
#         elif x>z and y>z:
#             c.append(max(x,y))
#         elif x>z and y<=z:
#             c.append(x)
#         elif x<=z and y>z:
#             c.append(y)
#         elif x<=z and y<=z:
#             if x!=z and y==z:
#                 c.append(x)
#             elif x==z and y!=z:
#                 c.append(y)
#     min_val=1
#     c.sort()
#     for x in c:
#         if x>min_val:
#             break
#         elif x==min_val:
#             min_val+=1
#     ans=min_val
#     return ans

from collections import defaultdict

def solution(A, B):
    n = len(A)

    # 값 x -> x를 선택할 수 있는 인덱스들의 목록
    pos = defaultdict(list)
    for i in range(n):
        x, y = A[i], B[i]
        if x > 0:
            pos[x].append(i)
        if y > 0 and y != x:
            pos[y].append(i)

    # 강제 m 존재 여부: 어떤 i에서 (A[i]==m and B[i]==m)
    def has_forced_m(m):
        for i in range(n):
            if A[i] == m and B[i] == m:
                return True
        return False

    # 이분 매칭: 왼쪽(숫자 x) -> 오른쪽(인덱스 i)
    # matchR[i] = 이 인덱스 i에 매칭된 숫자 x (없으면 -1)
    def can_cover_all_upto(m):
        matchR = [-1] * n

        # DFS로 증대 경로 탐색 (Kuhn 알고리즘)
        def dfs(x, seen):
            if x not in pos:
                return False
            for i in pos[x]:
                if seen[i]:
                    continue
                seen[i] = True
                if matchR[i] == -1 or dfs(matchR[i], seen):
                    matchR[i] = x
                    return True
            return False

        for x in range(1, m):
            # 각 x를 배정하기 위한 방문배열 초기화
            seen = [False] * n
            if not dfs(x, seen):
                return False
        return True

    # m은 1..N+1 범위에서만 보면 충분
    m = 1
    while m <= n + 1:
        # 1) 강제 m이 있으면 이 m은 절대 불가
        if has_forced_m(m):
            m += 1
            continue

        # 2) 존재성 검사: 1..m-1 중 pos[x]가 비면 MEX는 그 x
        missing_x = 0
        for x in range(1, m):
            if x not in pos or len(pos[x]) == 0:
                missing_x = x
                break
        if missing_x != 0:
            return missing_x

        # 3) 최대 매칭으로 1..m-1 모두 커버 가능?
        if can_cover_all_upto(m):
            return m

        m += 1

    # 이론상 도달하지 않음(반드시 1..N+1에서 결정)
    return n + 2

A=[1,2,4,3]
B=[1,3,2,3]
# A=[3,2,1,6,5]
# B=[4,2,1,3,3]
# A=[1,2]
# B=[1,2]
print(solution(A,B))