#!/usr/bin/env Python
# coding=utf-8
def check1(before,now):
    if before[-1]==now[0]:
        return True
    else:
        return False

def check2(now,dics):
    for dic in dics:
        if now in dic.keys():
            return False
    return True

def solution(n, words):
    answer = [0,0]

    dics=[dict() for _ in range(n)]
    dics[0][words[0]]=0

    for i in range(1,len(words)):
        order,num=divmod(i,n)
        before,now=words[i-1],words[i]
        dic=dics[num]
        if check1(before,now) and check2(now,dics):
            dic[now]=num
        else:
            answer=[num+1,order+1]
            break

    return answer

n=2
# words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
words=["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,words))