# list is a dataType that is a collection of other dataTypes
fruits = ['apple','pear',3]

# print out the entire list
print(fruits)

# print out one item of the list
print(fruits[1]) # [i], where i is the indice of the list of positions 0, 1 and 2

# add to the end of the list
fruits.append('banana')
print(fruits)

# change item at a specific index
fruits[2] = 'strawberry'
print(fruits)

# Tuple is another dataType, used for coordinates, colors and rectangles
position = (2,3)
rgb = (255, 255, 0)