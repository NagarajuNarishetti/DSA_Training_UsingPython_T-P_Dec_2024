arr=list(map(int,input().split()))

'''
for ele in arr:
    if arr.count(ele) > len(arr)/2:
        print(ele)
        break
'''

print(len(arr)," Length of arr")
dict1={}
for ele in arr:
    dict1[ele]=dict1.get(ele,0)+1
    if dict1[ele]>len(arr)/2:
        print(ele)
print(dict1)

