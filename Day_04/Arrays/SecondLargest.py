arr=list(map(int,input().split()))
m1=float('-inf')
m2=float('-inf')
m3=float('+inf')
for i in range(len(arr)):
    # m1=max(m1,arr[i])
    if arr[i]<m3:
        m3=arr[i]
    if arr[i]>m1:
        m2=m1
        m1=arr[i]
    elif arr[i]>m2 and arr[i]<m1:
        m2=arr[i]


# for ele in arr:
#     if ele<m1 and ele>m2:
#         m2=ele
print(*arr)
print(f"Largest ele is {m1}\n2nd largest ele is {m2}\nMinimum ele is {m3}")

# print(max(arr))