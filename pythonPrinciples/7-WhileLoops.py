#while loops
conditions = True
keepgoingtoomuch = 0

while conditions:
    print('Keep doing it, unless it is false or it breaks')
    keepgoingtoomuch += 1
    if keepgoingtoomuch > 4:
        break # this will get out of the loop
    if int(input('Guess the loop')) == keepgoingtoomuch:
        conditions = False # this will terminate the loop