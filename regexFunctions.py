import re

#This is the example that shows we can make custom character classes using regex 

email_Extractor = re.compile(r'\w{,}.?\w{,}@\w{,}.com')
my_email = email_Extractor.findall("Hi, this is Kushagra Dubey. I use four email ids; some are for my work and some for the personal use. I have an id named greatnamokushagra@gmail.com which I usually use for the personal use. And then I have another id named kushagradubey0602@gmail.com and kushagracreator02outlook.com which I use for the work. I have a one more id named tester.kd06@gmail.com which I use for software testing related puposes. Thank you and you can mail at any of the provided ids above.")
print(my_email)


consonantRegex = re.compile(r'cc[^aeiouAEIOU]') #placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class. 

mo1 = consonantRegex.findall('RoboCorp is the foundation of the robo corporation and it works in the AI field to make robots and help teh world in the advancement of techonology.')
print(mo1)

#Dollar and Caret Symbol - 

#can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex

# beginsWithHello = re.compile(r'^Hello')
# mo2 = beginsWithHello.search('Hello this is Kushagra')
# print(mo2)

# endsWithNumber = re.compile(r'\d$')#single number
endsWithNumber = re.compile(r'\d+$')#multiple number
mo3 = endsWithNumber.search('Your number is 12652626')
print(mo3)


#WildCard Character

atRegex = re.compile(r'.at')
mo4 = atRegex.findall('The cat in the hat sat is on the flat mat.')
print(mo4)


#Dot-Star

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #greedy way and put ? for the non-greedy way

mo5 = nameRegex.search('First Name: Kushagra Last Name: Dubey')
print(mo5.group(1))
print(mo5.group(2))


#Matching the Newline Character

newLineRegex = re.compile('.*', re.DOTALL)
mo6 = newLineRegex.search("Serve the god.\n He is the only almighty.\n Serve him so that you don't have to serve fools.")
print(mo6.group())


#Ignoring Case-Sensitivity with Regex

roboCop = re.compile(r'robocop', re.I)
mo7 = roboCop.search("RoboCop is part man, part machine, all cop.")
print(mo7.group())


#Substitutions String with sub() Method

namesRegex = re.compile(r'Agent \w+')
mo8 = namesRegex.sub('CENSORED', 'Agent Alice gave that secret to Agent Bob.') # replaces the given word to the desired word with the sub() method

print(mo8)


agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo9 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo9)

#Managing Complex Regexes

phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)''', re.VERBOSE)

#Combining re.IGNORECASE, re.DOTALL, re.VERBROSE

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
 
