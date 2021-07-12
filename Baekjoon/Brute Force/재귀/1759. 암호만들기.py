# recur(n,alpha,password,i)
# n : 만들어야 하는 암호 길이
# alpha : 사용할 수 있는 알파벳
# password : 현재까지 만든 암호
# i : 사용할지 말지 결정해야 하는 알파벳의 인덱스

# 경우의 수
# 1) 알파벳을 사용
#     i+=1
#     password += alpha[i]
#
#     recur(n,alpha,password + alpha[i], i+1)
#
# 2) 알파벳 사용 X
#     i+=1
#
#     recur(n,alpha,password,i+1)
#
# 3) 정답을 찾은 경우
#     n == len(password)
#
# 4) 불가능한 경우. 더 이상 사용할 수 있는 알파벳이 없는 경우
#     i>=len(alpha)

c,l = map(int,input().split())
result = [0]*l

arr = list(map(str,input().split()))
arr.sort()
index=0

vowels = ['a','e','i','o','u']
cons_used=0
vowel_used=False

def check(password):
    result=False
    cons_used=0
    vowel_used = False
    for ele in list(password):
        if ele not in vowels:
            cons_used+=1
        else:
            vowel_used=True
    if cons_used >= 2 and vowel_used == True:
        result=True

    return result

def recur(n,alpha,password,i):
    if n==len(password):
        if check(password):
            print(password)
        return
    if i>= len(alpha):
        return
    recur(n,alpha,password+alpha[i],i+1)
    recur(n,alpha,password,i+1)



recur(c,arr,'',0)