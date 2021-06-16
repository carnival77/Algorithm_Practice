a = "1223334444"

print(a)
print("a[:3] : " + a[:3]) # 지정한 인덱스 -1 까지
print("a[3:] : " + a[3:]) # 지정한 인덱스부터

b= '0000'



temp=''

temp2 = temp.join(list(map(lambda x: 0 if x==0 else '1', b)))

print(temp2)