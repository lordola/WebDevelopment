values = [1, 3, 4, "Lukman", 0.9, "age"]

print(values[3])
print(values[1])
#to print last value
print(values[-1])
#to insert
values.insert(4, "Ade")
print(values)
#to add to last value
values.append("old")
print(values)
#to retrive sub index
print(values[1:3])
#to update
values[3]= "LUKMAN"
#to add range
values[1:3]= ["Ola", "Dele"]
print(values)

#to remove one
values.remove(1)
#to remove by index
values.pop(0)
#to remove last index
values.pop()
print(values)
#to delete
del values[2]
print(values)

#to clear list
values.clear()
print(values)

#tuple: same as List, just that its in () and its immutable- values cant be updated



