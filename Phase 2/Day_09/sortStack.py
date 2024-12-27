arr=list(map(int,input().split()))
res=[]
while arr:
    curr=arr.pop()
    while res and res[-1]>curr:
        arr.append(res.pop())
    res.append(curr)
print(res)