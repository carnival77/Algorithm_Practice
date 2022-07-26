#!/usr/bin/env Python
# coding=utf-8
def solution(msg):
    ans = []
    # solution 1. 너무 길다.
    # msg=list(msg)
    # l = 1001
    # #1
    # dic=dict()
    # asc=65
    # for inx in range(1,27):
    #     dic[inx]=chr(asc)
    #     asc+=1
    # #2
    # while len(msg)>0:
    #     w=''
    #     num=0
    #     for i in range(1,l):
    #         ok = False
    #         tg="".join(msg[:i])
    #         for k,v in dic.items():
    #             if v==tg:
    #                 num=k
    #                 w=v
    #                 ok=True
    #         if not ok:
    #             break
    #     #3
    #     ans.append(num)
    #     for ele in list(w):
    #         msg.remove(ele)
    #     #4
    #     c=''
    #     if len(msg)>0:
    #         c=msg[0]
    #     inx+=1
    #     dic[inx]=w+c

    #solution 2.
    # dic={chr(i+64): i for i in range(1,27)}
    # while msg:
    #     i=1
    #     while msg[:i] in dic.keys() and i<=len(msg):
    #         i+=1
    #     i-=1
    #     ans.append(dic[msg[:i]])
    #     dic[msg[:i+1]]=len(dic)+1
    #     msg=msg[i:]

    #solution 3.
    dic={chr(i+64): i for i in range(1,27)}
    while True:
        if msg in dic.keys():
            ans.append(dic[msg])
            break
        for i in range(1,len(msg)+1):
            if msg[:i] not in dic.keys():
                ans.append(dic[msg[:i-1]])
                dic[msg[:i]]=len(dic)+1
                msg=msg[i-1:]
                break

    return ans

# msg="KAKAO"
# msg="TOBEORNOTTOBEORTOBEORNOT"
msg="ABABABABABABABAB"
print(solution(msg))