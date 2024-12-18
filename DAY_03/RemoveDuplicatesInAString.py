str=input()
set1=set()
new=""

'''for i in str:
    if i in set1:
        continue
    else :
     set1.add(i)
     new+=i
print(new)'''

for char in str:
    if char not in new:
        new+=char
print(new)

