def fizBuzz(n):
    if n%3==0:
        if n%5==0:
            return " FIZBUZZ"
        else:
            return" FIZZ"
    elif n%5==0:
        return " BUZZ"
    else:
        pass


n=int(input())
for i in range(1,n+1):
    print(i,fizBuzz(i))
