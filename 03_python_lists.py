# In this file we will look at lists, dictionaries, set, tuples, range.

# List 
myList =[1, 2, 3, 4, 5]
print(myList)

print(type(myList))

print(myList[0])

print(f'Our list object myList has {len(myList)} elements')

mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

mixedList.append(6)
print(mixedList)

mixedList.pop(0)

print(mixedList.reverse())