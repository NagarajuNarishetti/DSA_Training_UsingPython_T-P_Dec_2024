arr=list(map(int,input().split()))
arr.sort()
n=int(input("Ente n value to find nth max and nth min : "))
print(f"Nth smallest {arr[n-1]} \nNth Largest is {arr[-n]}")