myList = [1, 2, 'abc']

for i in range(5):
  print(i)

range_vals = [0, 1, 2, 3, 4]
print("Using a list to display values 0-4")
for i in range_vals:
  print(i)

for name in ['Alice', 'Bob', 'Charlie']:
  print(name)
  for letter in name:
    print(letter)

print("Using enumerate()")
for index, name in enumerate(['Alice', 'Bob', 'Charlie']):
  print(index, name)

myList = ['Alice', 'Bob', 'Charlie']
for index in range(len(myList)):
  print(index, myList[index])

print("Using a loop to create a list of capital letters from A-Z")

alphabet = []

for i in range(65, 91):
  print(i, chr(i))
  alphabet.append(chr(i))

print(alphabet)

i=0
while i<10:
  print(i)
  i+=1


# List comprehensions
squares = []
for num in range(0,11):
  squares.append(num**2)
print(squares)

squares = [num**2 for num in range(0,11) if num%2 == 0]