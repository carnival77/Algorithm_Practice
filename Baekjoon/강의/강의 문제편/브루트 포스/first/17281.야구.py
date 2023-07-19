import sys
from itertools import permutations

input=sys.stdin.readline

n=int(input())
eanings=[]
for _ in range(n):
    eanings.append(list(map(int,input().split())))

# 선수 번호는 0부터 센다.
arr=[1,2,3,4,5,6,7,8] # 0번 선수는 4번 타자로 고정이므로 나머지 선수들의 번호만 갖는다.
ans=0 # 최대 점수

# 선수들의 타순을 정한다. 0번 선수는 4번 타자로 고정이므로 나머지 선수들의 타순을 정하고 0번 선수를 4번 인덱스에 삽입한다.
for order in permutations(arr,8):
    order=list(order) # 선수들의 타순
    order.insert(3,0) # 0번 선수는 4번 타자로 고정
    num=0 # 타자 번호
    point=0 # 이번 이닝의 점수
    for eaning in eanings: # 각 이닝 동안
        out=0 # 아웃의 개수
        one,two,three=False,False,False # 1루, 2루, 3루 상태
        while True: # 각 선수들이 타순에 맞게 친다
            st=order[num]
            res=eaning[st] # 그 결과인 0,1,2,3,4에 따라 진루 및 득점과 아웃을 기록한다.
            if res==0:
                out+=1
                if out>=3:
                    num+=1
                    if num==9: # 타자 번호가 9가 되면 0으로 바꾼다.
                        num=0
                    break
            elif res==1:
                if three:
                    point+=1
                    three=False
                if two:
                    three=True
                    two=False
                if one:
                    two=True
                    one=False
                one=True
            elif res==2:
                if three:
                    point+=1
                    three=False
                if two:
                    point+=1
                    two=False
                if one:
                    three=True
                    one=False
                two=True
            elif res==3:
                if three:
                    point+=1
                    three=False
                if two:
                    point+=1
                    two=False
                if one:
                    point+=1
                    one=False
                three=True
            else:
                if three:
                    point+=1
                    three=False
                if two:
                    point+=1
                    two=False
                if one:
                    point+=1
                    one=False
                point+=1
            num+=1
            if num==9:
                num=0
    ans=max(ans,point) # 이번 타순으로 얻은 점수와 최대 점수 중 최댓값을 최대 점수로 설정하여 모든 타순의 경우의 수 중 최대 점수를 얻는다.

print(ans)