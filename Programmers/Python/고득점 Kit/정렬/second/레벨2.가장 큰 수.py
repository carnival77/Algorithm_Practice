# solution 1
def solution(numbers):
    answer=''

    str_nums=[str(x) for x in numbers]
    str_nums.sort(key=lambda x:(x*4)[:4], reverse=True)
    answer=''.join(str_nums)

    return answer

import functools

# solution 2
def comparator(a,b):
    t1=(int)(a+b)
    t2=(int)(b+a)
    return ((t1>t2) - (t1<t2))

def solution2(numbers):
    str_nums=[str(x) for x in numbers]
    str_nums.sort(key=functools.cmp_to_key(comparator),reverse=True)
    return str(int(''.join(str_nums)))