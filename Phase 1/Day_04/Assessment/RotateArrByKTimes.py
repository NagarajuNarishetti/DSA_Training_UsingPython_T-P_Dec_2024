arr=list(map(int,input().split()))
k =int(input()) # for k!=0 we can decrease the k value by appling mod with len(arr)

i =0

'''while i<k:
    temp=arr[0]
    for j in range(1,len(arr)):
        arr[j-1]=arr[j]
    arr[-1]=temp
    i+=1 '''

if arr:
    k%=len(arr)
for i in range(k):
    arr.append(arr[0])
    arr.pop(0)
print(arr) 
