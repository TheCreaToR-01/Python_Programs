import re

def isPhoneNumber(text):
    '''
    finds the indian phone numbers from the text
    1. 10 digits long
    2. +91 area code in the starting
    '''

    str = '+916396974123'

# if len(text) != 10:
#     return False

for i in range(str):
    print(i, str[i]) 
