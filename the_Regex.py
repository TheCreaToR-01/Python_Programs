import re

# phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})') # a regex object

# mo = phoneNumRegex.search('My phone number is 223-522-5224')
# print('Phone Number Found: ' + mo.group(1))
# print('Phone Number Found: ' + mo.group(2))
# print('Phone Number Found: ' + mo.group(0))
# print('Phone Number Found: ' + mo.group())
# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print("Area Code: " + areaCode)
# print("Main Number: " + mainNumber)

# phoneNumRegex2 = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
# mo = phoneNumRegex2.search('My mobile number is (344) 255-5223')
# print(mo.group(1))
# print(mo.group(2))


# heroRegex = re.compile(r'Batman | Tina Frey') #checks whether they are available or not and if not both are available then the one who has first occurence will appear in the result

# mo1 = heroRegex.search('I met Batman and Tina Frey on that event.')

# mo2 = heroRegex.search('I met Tina Frey and Batman on that event.')
# print(mo1.group())
# print(mo2.group())

# batRegex = re.compile(r'Bat(mobile|man|copter|bat)')
# mo = batRegex.search('Batmobile is my favorite car.')
# print(mo.group())
# print(mo.group(1))


#Optional Matching with Question Mark
# batRegex = re.compile(r'Bat(wo)?man')
# batRegex = re.compile(r'Bat(wo)*man') #matching zero or more with the star symbol(optional)

# batRegex = re.compile(r'Bat(wo)+man') #same as star but not optional
# mo1 = batRegex.search('The Adcentures of Batman')
# print(mo1 == None)
# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())

#Matching Specific Repetitions with Curly Brackets

haRegex = re.compile(r'(Ha){3,}') # can set the repetition ratio in curly brackets {3,max}, {1,3}(1 to 3), {min,5}
mo1 = haRegex.search('HaHaHaHaHa')
mo2 = haRegex.search('HaHaHa')
print(mo1.group())
print(mo2.group())

#Greedy and Nongreedy Matching
#Note - Python regex is automatically greedy and tries to extract max possible thing from the statement as we can show 

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo_greedy1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo_greedy1.group()) #it will extract the max matched string

#non-greedy way
nongreedHaRegex = re.compile(r'(Ha){3,5}?')
mo_nongreedy1 = nongreedHaRegex.search('HaHaHaHaHa')
print(mo_nongreedy1.group()) #will print min matched string

#findall() Method

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo_findAll = phoneNumRegex.findall('Hi, this is Kushagr Dubey. Anyone can contact me on 876-453-5445 or 234-546-3443.') #will extract out all the contact numbers based on the format we provided from the string
print(mo_findAll)
