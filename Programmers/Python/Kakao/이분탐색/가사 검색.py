from bisect import bisect_left, bisect_right

def count_by_range(arr,left_value,right_value):
    left_value = bisect_left(arr,left_value)
    right_value = bisect_right(arr,right_value)
    return right_value - left_value

def solution(words,queries):
    result=[]

    arr=[]
    reversed_arr=[]

    # 1. words를 개수별로 그룹 구분 ( 뒤집힌 words 도 저장 )
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    # 2. words 그룹들 sort
    arr.sort()
    reversed_arr.sort()

    # 3. bisect로 queries 내 특정 문자열 가진 word의 개수 세기
    for query in queries:
        # 3-1. queries에서 query가 만약 접두사에 ?가 있다면, 뒤집힌 word arr에서 뒤집은 query 의 ? 자리에 a와 z를 넣은 값들을
        # left, right value 로 넣어 bisect
        if query[0] == '?':
            result.append(count_by_range(reversed_arr,query.replace('?','a')[::-1],query.replace('?','z')[::-1]))
        # 3-2. query에서 만약 접미사에 ?가 있다면, word arr 에 대하여 다음 위와 같은 과정 수행
        else:
            result.append(count_by_range(arr,query.replace('?','a'),query.replace('?','z')))