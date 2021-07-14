n= int(input())

t_arr=[0]*(n)
p_arr=[0]*(n)

for i in range(n):
    t_arr[i],p_arr[i] = map(int,input().split())

p=0

def recursive(i,sum,n,t_arr,p_arr):
    global p
    if i==n:
        if p<sum:
            p=sum
        return
    if i>n:
        return
    recursive(i+1,sum,n,t_arr,p_arr)
    recursive(i+t_arr[i],sum+p_arr[i],n,t_arr,p_arr)

recursive(0,0,n,t_arr,p_arr)
print(p)