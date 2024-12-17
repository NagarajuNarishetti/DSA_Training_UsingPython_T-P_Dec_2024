# tupel is immutable 
tuple1=('Student',1,1,0,True)

#Tuple is ordered i.e elements are in the given order

print(tuple1[0:3])
# to mute or edit 
''' convert form tuple to list and edit and convert back to tuple'''

list1=list(tuple1)
list1.remove('Student')
list1.insert(0,"Faculty")

tuple1= tuple(list1)

print(tuple1)

tuple1=tuple(list(tuple1).append("add"))

print(tuple1)