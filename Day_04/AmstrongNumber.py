def arm(n):
    temp=n
    sum=0
    while n!=0:
        sum+=(n%10)**3
        n//=10
    return sum==temp

n=int(input())
for i in range(n):
    if arm(i):
        print(i)
