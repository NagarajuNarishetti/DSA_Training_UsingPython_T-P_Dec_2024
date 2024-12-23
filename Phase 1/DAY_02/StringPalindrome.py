str=input("Enter String : ")
i=0
ispal=True
## or k=str[::-1] gives the reverse of str
while(i<len(str)/2):
    if(str[i]!=str[len(str)-i-1]):
        print("Not Palindrome")
        ispal=False
        break
    i+=1
if ispal:
    print("Is palindrome")
