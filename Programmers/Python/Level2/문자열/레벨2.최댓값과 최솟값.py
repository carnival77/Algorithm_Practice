def solution(s):
    answer = ''

    nums = list(map(int,s.split()))

    max_val = max(nums)
    min_val = min(nums)

    answer=str(min_val)+' '+str(max_val)

    return answer

s = "-1 -2 -3 -4"

print(solution(s))