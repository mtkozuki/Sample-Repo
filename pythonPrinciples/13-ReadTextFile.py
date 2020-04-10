# file.io
file = open('13.txt', 'r')

#\n get into
f = file.readlines()
print(f)

# One way to clear backlash n
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)

# strip
newList2 = []
for line in f:
    newList2.append(line.strip('\n'))

print(newList2)

# necessary
file.close()