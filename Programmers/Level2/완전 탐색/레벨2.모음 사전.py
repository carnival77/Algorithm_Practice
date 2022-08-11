from itertools import product

def solution(word):
    arr= {'A', 'E', 'I', 'O', 'U'}
    words='AEIOU'
    for i in range(4):
        for prd in product(arr,words):
            arr.add("".join(list(prd)))
    result = list(arr)
    result.sort()
    answer=result.index(word)+1

    return answer

from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1

# word="AAAAE"
# word="AAAE"
# word="I"
word="EIO"
print(solution(word))

