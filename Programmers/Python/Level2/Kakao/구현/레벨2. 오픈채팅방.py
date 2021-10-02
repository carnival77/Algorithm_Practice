def solution(record):
    answer = []

    DB = dict()

    for rec in record:
        rec=list(map(str,rec.split()))
        cmd=rec[0]
        if cmd=="Leave":
            continue
        uid=rec[1]
        nick=rec[2]
        DB[uid]=nick

    in_msg="님이 들어왔습니다."
    out_msg="님이 나갔습니다."

    for rec in record:
        rec=list(map(str,rec.split()))
        cmd=rec[0]
        uid=rec[1]
        if cmd=="Leave":
            answer.append("".join(DB[uid]+out_msg))
        elif cmd=="Enter":
            answer.append("".join(DB[uid]+in_msg))


    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))