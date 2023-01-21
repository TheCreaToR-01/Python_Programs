# helloFile = open('D:\\Automate_Boring_Stuff_Python\\plainFile.txt', 'r')
# helloContent = helloFile.read()
# print(helloContent)


# fileOpen2write = open('sonnet29.txt', 'w') # Writing the contents in the file(overwrites)
# print(fileOpen2write.write('Hi, I am learning Python for go for a job of Software Developer.\n'))
# fileOpen2write.close()

fileOpen2Append = open('sonnet29.txt', 'a') # Append mode to append the data in the file(appends data with the previous)
print(fileOpen2Append.write('I like to learn technology and technical things, gadgets, digital products etc.\n'))
fileOpen2Append.close()


fileOpen2Read = open('sonnet29.txt', 'r') # Reading the contents of the file
# print(fileOpen2Read.read())

import shelve
shelfLife = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfLife['cats'] = cats
shelfLife.close()

shelfLife = shelve.open('mydata')
type(shelfLife)
print(list(shelfLife.keys()))
print(list(shelfLife.values()))
print(shelfLife['cats'])