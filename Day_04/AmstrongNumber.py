# import math
def arm(n):
    temp=n
    sum=0
    # p=int(math.log10(n))+1 will give error for n=0
    p=len(str(n))
    while n!=0:
        sum+=(n%10)**p
        n//=10
    return sum==temp

n=int(input())
for i in range(n):
    if arm(i):
        print(i)
        