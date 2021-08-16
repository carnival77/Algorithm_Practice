a,b,c = map(int,input().split())

first = (a+b)%c
print(first)
second = ((a%c) + (b%c))%c
print(second)
third = (a*b)%c
print(third)
fourth = ((a%c) * (b%c))%c
print(fourth)