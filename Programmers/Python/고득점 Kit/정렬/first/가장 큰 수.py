# 1. comparator 함수 생성
#
# import functools
#
# def comparator(a,b):
#     t1=a+b
#     t2=b+a
#
#     return (int(t1) > int(t2)) - (int(t1)<int(t2))
#
# def solution(numbers):
#     answer = ''
#
#     arr = [str(x) for x in numbers]
#
#     arr = sorted(arr,key=functools.cmp_to_key(comparator),reverse=True)
#
#     answer=str(int(''.join(arr)))
#
#     return answer

# 2. 람다식 사용
#
# from functools import cmp_to_key
#
# def solution(numbers):
#     # 1. int형 배열인 numbers를 문자열 배열로 전환
#     numbers= [str(x) for x in numbers]
#     # 2. numbers 내의 요소들 중 두 개의 문자열을 합쳤을 때 더 큰 숫자 순으로 정렬
#     numbers = sorted(numbers, key=cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse=True)
#     # 3. 문자열 배열을 합치고 int 형으로 바꾼 다음 문자열로 다시 변환해 return
#     return str(int(''.join(numbers)))

# 3.
# 3.1 numbers를 문자열로 치환한다.
# 3.2 각 원소를 "무수히 많이 반복하여 길이를 4로 자른 문자열" 기준으로 numbers를 정렬합니다.
# 3.3 문자열을 합쳐줍니다.

from functools import cmp_to_key

def solution(numbers):
    numbers= [str(x) for x in numbers]
    numbers.sort(key=lambda x:(x*4)[:4],reverse=True)
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    numbers=[6, 10, 2]
    numbers=[3, 30, 34, 5, 9]

    print(solution(numbers))