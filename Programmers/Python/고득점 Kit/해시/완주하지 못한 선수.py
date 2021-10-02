def solution(participant, completion):

    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c:
            return p
    return participant.pop()

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))