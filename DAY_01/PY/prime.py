'''def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to √n, skipping multiples of 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True  # If no divisors found, the number is prime


# Input from the user
n = int(input("Enter a number: "))

# Check and print result
if is_prime(n):
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is Not a Prime Number")
    '''

n =int(input())
if n<1:
    print("Not a prime")
elif n<=3:
    print("Prime")
elif n%2==0 or n%3==0:
    print("Not Prime")
else :
    isPrime=True
    for i in range(5,(int)(n**0.5)+1,6):
        if(n%i==0 or n%(i+2)==0):
            print("Not Prime")
            isPrime=False
            break
    if isPrime :
        print("Prime")