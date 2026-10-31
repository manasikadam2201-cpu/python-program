a=[12,43,54,55,66,68,79]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even-",even)
print("odd-",odd)
