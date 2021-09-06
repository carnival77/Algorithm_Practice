tg = input()

alp = []
num=0

for ele in tg:
    if ele.isalpha():
        alp.append(ele)
    else:
        num+=int(ele)

alp.sort()

result = ''.join(alp)
result+=str(num)

print(result)