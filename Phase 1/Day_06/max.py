arr=list(map(int,input().split()))
mce=0
mc=0
for ele in arr:
    if arr.count(ele) >mc:
        mce=ele
        mc=arr.count(ele)
print(mce)
