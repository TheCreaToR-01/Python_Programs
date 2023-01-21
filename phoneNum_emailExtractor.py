#! python
#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import email
import math
import pyperclip, re
#phoneNumberRegex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #Area Code(optional)
    (\s|-|\.)?         #Separator(optional)
    (\d{3})            #Another digit(not optional)
    (\s|-|\.)          #Separator(not optional)
    (\d{4})            #Last four digits(not optional)
    (\s*(ext|x|ext.)\s*(\s{2,5}))? #extension(optional)
)''', re.VERBOSE)

#E-mail Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username
    @
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4}) #dot-something
)''', re.VERBOSE)


#Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# Hi, this is the demo text to check the code and here I am providing my email ids and contact number. 639-697-4123 , 905-854-3587 I have 4 email ids greatnamokushagra@gmail.com, kushagradubey0602@gmail.com, tester.kd06@gmail.com, kushagracreator02@outlook.com. I have two phone numbers called.

