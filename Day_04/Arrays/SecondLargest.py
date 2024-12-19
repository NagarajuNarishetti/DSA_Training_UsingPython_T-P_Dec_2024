arr=list(map(int,input().split()))
m1=float('-inf')
m2=float('-inf')
for i in range(len(arr)):
    m1=max(m1,arr[i])

for ele in arr:
    if ele<m1 and ele>m2:
        m2=ele
print(*arr)
print(f"Largest ele is {m1}\n2nd largest ele is {m2}")

# print(max(arr))