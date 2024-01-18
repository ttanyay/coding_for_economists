# Sets

mySet = {1, 2, 3} 
print(mySet)

print(type(mySet))

mySet = {1, 2, 3, 3} 
print(mySet)

print(1 in mySet)

print(set('aaaaaaaaaaaabbbbbccc'))


setA = {1, 2, 3}
listB = [3, 4, 5, 5, 5, 5, 5]
setB = set(listB)

print(setA, setB)

unionAB = setA | setB
print(unionAB)

intersectionAB = setA & setB
print(intersectionAB)