1.1. 함수의 인자 : 다음 요소를 선택할 때 영향을 미치거나 고려해야 하는 것. 변하는 것.
    후보 :
    1. index. 몇 번째
    2. cnt. 개수
    3. sum. 현재 전체 합
    4. n. 목표 길이
    5. arr. 주어진 요소들
    6. start. 오름차순일 경우 시작점.
    7. set. 집합

1.2. 전역 변수 : 함수의 인자, 주어진 변수(n,m) 등

2. 함수 내 재귀함수의 인자 변화
    1) index -> index+1
    2) sum -> sum + 현재요소

3. 템플릿 - 요소 간 순서가 중요하다.
3.1. 만약 주어진 집합 S의 원소가 오름차순이 아닌데, 출력은 사전 순이나 오름차순으로 해야 한다면, 집합 S 를 sort()하여 오름차순으로 바꿔준다.

    문제 : n개인 nums 배열 중 m개를 선택.

    # 순열 문제. 순열 : N개의 수 중 M개를 순서 상관하여 중복 허용하지 않고 뽑는다.
    # 즉, 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 취급한다.

    [template 1]

    used = [False] * n
    arr = [0]*m

    def dfs(index, 변화하는 요소 1, 변화하는 요소 2):

        # 종료 조건 설정
        # 정답을 찾은 경우
        if len(arr) == n:
            return
        # 불가능한 경우 = 더 이상 진행되면 index 에러가 나는 경우.
        if index > n:
            return

        for i in range(n):
            # 중복 허용 여부.
            if used[i]:
                continue
            # index 번째를 고르고 다시 돌려놓는 과정
            # i번째를 index 번째로 고름 = dfs 함수 호출 준비
            used[i]=True
            arr[index]=nums[i]
            dfs(index+1, 요소 1, 요소 2)
            used[i]=False

    # 조합 문제. 조합 : N개의 수 중 M개를 순서 상관하지 않고 중복 허용하지 않고 뽑는다.
    # 추가 조건 : 오름차순

    [template 1]

    def dfs(index, start, 변화하는 요소 2):

        # 종료 조건 설정
        # 정답을 찾은 경우
        if len(arr) == n:
            return
        # 불가능한 경우
        if index > n:
            return

        for i in range(start,n):
            # 중복 허용 여부.
            if used[i]:
                continue
            # index 번째를 고르고 다시 돌려놓는 과정
            # index 번째를 고름 = dfs 함수 호출 준비
            used[i]=True
            arr[index]=nums[i]
            dfs(index+1, i+1, 요소 2)
            used[i]=False

    [template 2]

    def dfs(index, 변화하는 요소 1, 변화하는 요소 2):

        종료 조건 설정
        # 정답을 찾은 경우
        if len(arr) == n:
            return
        # 불가능한 경우
        if index > n:
            return


        dfs(index+1, 변화하는 요소 1 변화 O, 변화하는 요소 2 변화 X)
        dfs(index+1, 변화하는 요소 1 변화 X, 변화하는 요소 2 변화 O)

        dfs(index+1, arr+[nums[index]])
        dfs(index+1, arr)

    # 중복순열 문제. 조합 : N개의 수 중 M개를 순서 상관하여 중복 허용하여 뽑는다.

    def dfs(index, 변화하는 요소 1, 변화하는 요소 2):

        종료 조건 설정
        # 정답을 찾은 경우
        if len(arr) == n:
            return
        # 불가능한 경우
        if index > n:
            return

        for i in range(n):
            # 중복 허용 여부.
            # if used[i]:
              #  continue
            # index 번째를 고르고 다시 돌려놓는 과정
            # index 번째를 고름 = dfs 함수 호출 준비
            used[i]=True
            arr[index]=nums[i]
            dfs(index+1, 요소 1, 요소 2)
            used[i]=False


    # 중복조합 문제. 조합 : N개의 수 중 M개를 순서 상관없이 중복 허용하여 뽑는다.
    # 추가 조건 : 오름차순

    def dfs(index, start, 변화하는 요소 2):

        종료 조건 설정
        # 정답을 찾은 경우
        if len(arr) == n:
            return
        # 불가능한 경우
        if index > n:
            return

        for i in range(start,n):
            # 중복 허용 여부.
            # if used[i]:
              #  continue
            # index 번째를 고르고 다시 돌려놓는 과정
            # index 번째를 고름 = dfs 함수 호출 준비
            used[i]=True
            arr[index]=nums[i]
            dfs(index+1, i+1, 요소 2)
            used[i]=False