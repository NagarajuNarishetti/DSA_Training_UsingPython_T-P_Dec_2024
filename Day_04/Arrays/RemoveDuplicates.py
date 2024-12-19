arr=list(map(int ,input().split()))
# print(*set(arr))
# for ele in arr:
set1=set()
# for i in range(len(arr)):
#     if arr[i] in set1:
#         arr.pop(i)
#         # i-=1
#     else:
#         set1.add(arr[i])
i=0
while i<len(arr):
    if arr[i] in set1:
        arr.pop(i)
    else :
        set1.add(arr[i])
        i+=1
        
print(*arr)