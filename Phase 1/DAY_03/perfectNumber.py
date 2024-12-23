n=int(input())
def isPerfect(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    return sum==n

for i in range(1,n):
    if isPerfect(i):
        print(i)
