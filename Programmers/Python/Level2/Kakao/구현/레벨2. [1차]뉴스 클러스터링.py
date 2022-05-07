from collections import Counter

# solution 1. Counter 사용
def solution(str1, str2):

    # 다중 집합 만들기
    # 1. 각 str의 list 만들기
    one_set=[]
    two_set=[]
    # 2. 각 문자열을 두 글자씩 끊어서, isalpha() 가 true인 것만 넣기
    for i in range(1,len(str1)):
        pair = str1[i-1:i+1]
        if pair.isalpha():
            one_set.append(pair.upper())
    for i in range(1,len(str2)):
        pair = str2[i-1:i+1]
        if pair.isalpha():
            two_set.append(pair.upper())

    one_cnt = Counter(one_set)
    two_cnt = Counter(two_set)

    # 3. 자카드 유사도 구하기.
    # 둘 다 공집합일 경우 j = 1
    if len(one_cnt) ==0 and len(two_cnt) ==0:
        j=1
    else:
        intersection = list((one_cnt & two_cnt).elements())
        union= list((one_cnt | two_cnt).elements())

        j = len(intersection)/len(union)

    answer = int(j*65536)
    return answer


str1="E=M*C^2"
str2="e=m*c^2"
print(solution(str1,str2))

# solution 2. Counter + 파이써닉
from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer