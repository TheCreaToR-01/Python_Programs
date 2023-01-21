#Raw Strings - escape character can be ingnored in this string

print(r'That is Carol\'s cat.') #Raw String

print("""
Dear Alice, 

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely, 
BOB
""")  # This is multi-line string

"""This
 is the 
 multi-line comment
"""

"""Strings can also be indexed in he same way as the lists"""

spam = "Hello World"
print(spam[:11]) #slicing and indexing of the string it excludes the last like above 10th index will be excluded
print('H' in spam)
print('O' not in spam) 
spam = spam.upper() #converts to upper case
spam = spam.lower() #converts to lower case
print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great': # handling user's input variations
    print('I feel great too!')
else:
    print("I hope the rest of your dau will be good.")

print(spam.islower()) #checks the condition
print(spam.isupper()) #checks the condition