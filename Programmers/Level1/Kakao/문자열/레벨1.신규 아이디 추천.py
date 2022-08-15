def solution(new_id):
    #1
    answer=new_id.lower()
    #2
    tmp=''
    target=['-','_','.']
    for a in answer:
        if a.isalpha() or a.isdigit() or a in target:
            tmp+=a
    answer=tmp
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if answer[0]=='.': answer=answer[1:]
    elif answer[-1]=='.': answer=answer[:-1]
    elif len(answer)==1 and answer[0]=='.': answer=''
    #5
    if answer=='': answer='a'
    #6
    if len(answer)>=16: answer=answer[:15]
    # if answer[0]=='.': answer=answer[1:]
    if answer[-1]=='.': answer=answer[:-1]
    #7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

# new_id="...!@BaT#*..y.abcdefghijklm"
# new_id="z-+.^."
new_id="=.="
print(solution(new_id))