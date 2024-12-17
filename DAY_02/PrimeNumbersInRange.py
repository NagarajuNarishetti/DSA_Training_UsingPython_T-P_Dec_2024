a1,a2=list(map(int,input().split()))

def isPrime(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3 ==0:
        return False
    for i in range (5,(int(n**0.5))+1,6):
        if n%i==0 or n%(i+2)==0 :
            return False
    return True

print()
for i in range(a1,a2) :
  if isPrime(i):
    print(i)