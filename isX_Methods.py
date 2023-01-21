name = "Helo this is Kushagr6702"
print(name.isalpha()) # checks if string is alpha or not(False if spaces and special char found)

print(name.isalnum()) # checks if str has only letters and numbers without spaces

print(name.isdecimal()) #True - if str has only numeric value without space

print(name.isspace()) #checks the spaces, tabs and returns True if only these are present and not blank

ttl = "This Is The Title"
print(ttl.istitle()) # if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

print(name.startswith('Helo')) #checks whether the given str starts with the given argument or not
print(name.endswith('02')) # checks if it ends with 02 or not


print(' '.join(['My', 'name', 'is', 'Kushagr', '6702'])) # inserts the desired thing btween the given list provided

print('ABC'.join(['I', 'am', 'a', 'student.'])) # inserts ABC between the list words

print('My name is Kushagra 6702'.split(' ')) # it is opposite to the join function

spam = """Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob"""
print(spam.split('\n'))

print("'Hello'".rjust(10, '*')) # justifies the text by adding 5 more spaces to make 10 to the left side
print("'Kushagr'".ljust(10)) #justifies the text by adding spaces to the right side
print('Kushagr_6702'.center(20, '*')) #center justify just as the above alignments
