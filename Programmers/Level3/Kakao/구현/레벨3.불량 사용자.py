from itertools import product,permutations
from collections import defaultdict
from copy import deepcopy

def solution(user_id, banned_id):
    answer = set()
    # arr=set(list(str(i) for i in range(10)))
    # for user in user_id:
    #     for a in list(user):
    #         arr.add(a)
    # print(arr)
    d=defaultdict(set)

    for id in banned_id:
        # id=list(id)
        target_inx=[]
        for inx,a in enumerate(list(id)):
            if a=='*':
                target_inx.append(inx)
        n=len(target_inx)
        # cnt=0
        l=len(id)
        arr=set()
        targets=[]
        for user in user_id:
            if len(user)==l:
                targets.append(user)
                for a in list(user):
                    arr.add(a)
        # sames=set()
        for perm in product(arr,repeat=n):
            tmp_id=list(id[:])
            for i,inx in enumerate(target_inx):
                tmp_id[inx]=perm[i]
            # print(id)
            same=''.join(map(str,tmp_id))
            # if same in targets:
            for target in targets:
                if same==target:
                # cnt+=1
                # sames.append(same)
                # sames.add(same)
                    d[id].add(target)
        # if cnt>0:
        #     answer*=cnt

    print(d)

    for perm in permutations(banned_id,len(banned_id)):
        res=set()
        tmp=deepcopy(d)
        res_list=[]
        for id in perm:
            tmp_list=list(tmp[id])
            for i in range(len(tmp_list)):
                v=tmp_list[i]
                if v not in res_list:
                    # res.add(v)
                    res_list.append(v)
                    tmp[id].remove(v)
                    if not tmp[id]:
                        break
                else:
                    continue
        answer.add(tuple(sorted(res_list)))

    print(answer)


    # result=[v for v in d.values()]
    # print(result)

    # for i in range(len(result)-1):
    #     res=set()
    #     for v in result[i]:


    # for i,k in enumerate(d.keys()):
    #     result=set()
    #     for v in

    # result=set()
    # for id in d.keys():
    #     for comb in combinations(d[id].values(),1):
    #         result.add(str(comb))


    return len(answer)

# user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id=["fr*d*", "abc1**"]
banned_id=["*rodo", "*rodo", "******"]

print(solution(user_id,banned_id))