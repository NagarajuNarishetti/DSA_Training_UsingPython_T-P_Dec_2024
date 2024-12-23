arr=list(map(int,input().split()))
flag=1
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        continue
    else:
        flag=0
        
if flag:
    print("IS Sorted")
else:
    print("is Not sorted")

print(arr==sorted(arr))
