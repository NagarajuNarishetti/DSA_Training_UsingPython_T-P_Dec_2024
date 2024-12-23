arr=[1,2,3,3,4,5]

s=((len(arr)*(len(arr)+1)))//2
print(s)
print(f"Repated Number = {sum(arr)-sum(set(arr))}")
print(f"Missing Number = {s-sum(set(arr))}")