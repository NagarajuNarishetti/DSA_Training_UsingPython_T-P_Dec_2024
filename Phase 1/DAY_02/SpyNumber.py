n=int(input("Enter a Number : "))
t=n
sum=0
mul=1
while n!=0:
    temp=n%10
    sum+=temp
    mul*=temp
    n=n//10

print(f"Sum if {sum} Pro is {mul}")

if(t==0):
    print("True")
else:
    print(sum==mul)
