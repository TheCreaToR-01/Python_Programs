def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '*'))

picnicItems = {'sandwiches': 400, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 6)
printPicnic(picnicItems, 20, 6)

str = '     Hello World          '
print(str.lstrip()) # clears all spaces from the left
print(str.rstrip()) # clears all spces from the right
print(str.strip()) # clears all spaces from both sides

str2 = 'SpamSpamBaconSpamEggsSpamSpam'
print(str2.strip('ampS')) # clears given input from both sides of the string