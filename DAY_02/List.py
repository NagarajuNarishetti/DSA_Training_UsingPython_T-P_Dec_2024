list1=[True,False,'Python',5,5.0]

# List is ordered
print(list1[0])
print(list1[2])

# List is mutable
list1[0]='a'
print(list1)

#append 
''' in append we need to include value append(value)'''

list1.append(2)
print(list1)

# insert at index
''' Insert method accepts two paramers index and input'''
list1.insert(2,'two')
print(list1)

# Extend

list2=[1,2,3,4,5]

list1.extend(list2)

print(list1)
print(list2)

# Removing the elements

''' remove is used to remove the value when you want to remove the value'''

list1.remove(2) # removes 1st ocuuring element wiht given value in the list 
print(list1)
list1.pop(4) # removes element at index 4
print(list1)

#Slicing

print(list1[:])
print(list1[1:])
print(list1[1])
