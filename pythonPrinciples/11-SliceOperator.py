fruits = ['apples', 'pear', 'strawberrys']
text = 'Hello I like python'

# It will slice somthing 
# Syntax: [start:end]
print(text[:4])

# Step[::n]
print(text[::2])

# Insert between something 
#fruits.append('b') = fruits[2:2] = 'b' would insert b between pear and strawberrys
fruits[1:1] = 'banana' # will inser each letter of banana as an item between apples and pear
print(fruits)