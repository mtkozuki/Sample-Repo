# Chained conditions is just adding conditions with AND or OR
x = 2
y = 3
if x == y and x + y == 5:
    print('Both are true') # nope

if x == y or x + y == 5:
    print('At least one is true') # yep

# not reverses all
if not(x == y and x + y == 5):
    print('Both are false') # yep

# nested statement
if x == 2:
    if y == 4:
        print('Both are true')
    else:
        print("First is true, Second isn't") # x
else:
    print('First is false')