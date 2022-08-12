#!/usr/bin/env Python
# coding=utf-8

# 시간 초과. 왜냐하면, 1 ≤ numbers의 길이 ≤ 100,000 , 0 ≤ numbers의 모든 수 ≤ 10^15 이므로,
# 10만 개의 10^15 값의 수의 이진수의 각 비트를 비교하는 것은 시간 초과다.
# def solution(numbers):
#     answer = []
#     MAX=bin(int(1e9))[2:]
#
#     for number in numbers:
#         ans=MAX
#         n=number
#         while ans==MAX:
#             n+=1
#             bin_number=str(bin(number)[2:])
#             bin_n=str(bin(n)[2:])
#             dif=abs(len(bin_number)-len(bin_n))
#             bin_number = '0'*dif+bin_number
#             cnt=0
#             for x,y in zip(bin_number,bin_n):
#                 if x!=y:
#                     cnt+=1
#             if cnt<=2:
#                 ans=min(ans,bin_n)
#         answer.append(int(ans,2))
#
#     return answer

# solution. 짝수/홀수별 규칙을 찾는다.
# 주어진 number의 이진수인 bin_number에서,
# number가 짝수일 경우와 홀수일 경우를 모두 대비해 맨 왼쪽에 '0'을 붙여준다
# rfind로 bin_number의 맨 오른쪽부터 '0'의 인덱스 idx를 찾고,
# 짝수의 경우, idx의 수를 '0'에서 '1'로 바꾼다.
# 홀수의 경우, idx의 수를 '0'에서 '1'로 바꾸고,
# idx+1의 수를 '1'에서 '0'으로 바꾼다.

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number=list('0'+bin(number)[2:])
        idx=''.join(bin_number).rfind('0')
        bin_number[idx]='1'
        if number%2==1:
            bin_number[idx+1]='0'
        answer.append(int(''.join(bin_number),2))

    return answer

numbers=[2,7]
print(solution(numbers))