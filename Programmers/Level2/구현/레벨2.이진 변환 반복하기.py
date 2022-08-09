# import string
# tmp=string.digits+string.ascii_uppercase
# def convert(num,base):
#     q,r=divmod(num,base)
#     if q==0:
#         return tmp[r]
#     else:
#         return convert(q,base)+tmp[r]
#
# def solution(s):
#     cnt1=0
#     cnt2=0
#     while s!='1':
#         tmp=''
#         for n in s:
#             if n=='0':
#                 cnt2+=1
#             else:
#                 tmp+=n
#         s=convert(len(tmp),2)
#         cnt1+=1
#     answer=[cnt1,cnt2]
#     return answer

def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

s="110010101001"
print(solution(s))