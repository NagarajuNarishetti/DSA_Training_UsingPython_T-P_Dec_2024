s1="eeeeeeffee"
s=input("Enter char to check : ")
count=0

'''for i in range(0,len(s1)):
    if(s1[i]==s):
        count+=1'''

for i in s1:
    if i==s:
        count+=1
print(count)

print(s1.count(s))
