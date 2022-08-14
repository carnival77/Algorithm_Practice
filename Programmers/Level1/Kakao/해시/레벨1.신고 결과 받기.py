# from collections import defaultdict
#
# def solution(id_list, report, k):
#
#     d1 = dict()
#     d2 = defaultdict(set)
#     d3 = dict()
#
#     for id in id_list:
#         d1[id] = 0
#         d3[id] = 0
#
#     for data in report:
#         a, b = data.split()
#         d2[a].add(b)
#
#     for values in d2.values():
#         for v in values:
#             d1[v] += 1
#
#     for key,v1 in d2.items():
#         for v2 in v1:
#             if d1[v2]>=k:
#                 d3[key]+=1
#
#     return list(v for v in d3.values())

from collections import defaultdict

def solution(id_list, report, k):
    answer=[0]*len(id_list)
    user = defaultdict(set)# user별 신고한 id 저장
    cnt=defaultdict(int)# user별 신고당한 횟수 저장

    for r in set(report): # 중복 신고 제거
        a,b=r.split()
        user[a].add(b)# 신고자가 신고한 id 추가
        cnt[b]+=1# 신고당한 id의 신고 횟수 추가

    for inx,id in enumerate(id_list):
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[id]:
            if cnt[u]>=k:
                answer[inx]+=1

    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 2
k = 3
print(solution(id_list, report, k))
