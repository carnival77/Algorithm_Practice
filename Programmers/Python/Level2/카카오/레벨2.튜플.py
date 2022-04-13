def solution(s):
    answer=[]

    l = s.lstrip('{').rstrip('}').split('},{')

    a=[[] for _ in range(len(l))]

    for i in range(len(l)):
        tmp=l[i].split(",")
        a[i]=tmp

    a.sort(key=len)

    for ele in a:
        for e in ele:
            if e not in answer:
                answer.append(e)

    answer=list(map(int,answer))

    return answer

# s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s="{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s="{{20,111},{111}}"
# s="{{123}}"
s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))