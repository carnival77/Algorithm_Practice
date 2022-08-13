# def solution(strings, n):
#     strings = sorted(strings)
#
#     sdict = {0: strings[0]}
#
#     for i in range(1, len(strings)):
#         sdict[i] = strings[i]
#
#     answer = list(dict(sorted(sdict.items(), key=lambda x: x[1][n])).values())
#
#     return answer

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])