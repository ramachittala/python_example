

allguests = {'Alias': {'apples': 5, 'banana': 5 }, 
             'Bose':{'cups': 3, 'apples': 6},
              'cati':{'plates': 5, 'apples': 2}}

def totalBrought(guests, item):
    numBrough = 0
    for k, v in guests.item():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('No of things being brought:')
print('apples' + str(totalBrought(allguests, 'apples')))


