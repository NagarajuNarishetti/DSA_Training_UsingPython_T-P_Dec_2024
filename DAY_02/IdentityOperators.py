# is and is not

''' expected result is boolean  it cheks wether the element belong to same object or not if the provided elements belong to same object it will return true else it will return false '''

print(1 =='1') # False
print(1 is '1') # False

list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2) # False
print(list1 == list2)  # True
print(list1 is not list2) # True