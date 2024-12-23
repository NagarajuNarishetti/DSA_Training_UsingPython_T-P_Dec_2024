str=input()
str2=""
for i in range(0,len(str)):
    if str[i]==str[i].upper():
        str2+=str[i].lower()
    else:
        str2+=str[i].upper()

print(str2)
print("Swap Case:", str.swapcase())  
