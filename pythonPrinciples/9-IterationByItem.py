# two type of for loops
fruits = ['apples', 'pears' , 'strawberrys']

#Iterations through list item rather than index
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not a pear')

#Iterations through index
for x in range(len(fruits)):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')