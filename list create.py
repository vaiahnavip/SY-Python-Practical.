list = [1,2,3,"vaishnavi","aditi","isha"]
print(list)
list.append(1)
print(list)
list.insert(2,5)
print(list)
list[2]=10
print(list)
list.extend([4,5,6,"a"])
print(list)
list.remove(10)
print(list)
list.pop(2)
print(list)
list.pop()
print(list)
del list[1]
print(list)
print(len(list))
if 1 in list:
    print("element is present")
else:
    print("element is not present")
    
for i in list:
    print(i)
    
print(list.count(4)) 
print(list.index(6)) 
  
list2=[5,8,3,2,1]
list2.sort()
print(list2)

list2.sort( reverse = True)
print(list2)

new_list2=list2.copy()
print(new_list2)

list.clear()
print(list)
