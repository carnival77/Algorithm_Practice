info = [[1,5],[3,5],[7,8]]

n = len(info)

# check = [[0] * 86399 for _ in range(n)]
seconds = [0] * 86400

for inx, case in enumerate(info):
    start = case[0]
    end = case[1]
    for i in range(start,end+1):
        # check[inx][i] +=1
        seconds[i] +=1

max_sc = max(seconds)
answer=[]

for inx,val in enumerate(seconds):
    if val == max_sc:
        answer.append(inx)

print(answer)