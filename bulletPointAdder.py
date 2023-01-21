# Adds bullets Points before the text

import pyperclip
text = pyperclip.paste() # pastes the copied data to the clipboard

lines = text.split('\n') # splits the lines from the new line character

for i in range(len(lines)): # loop through all the indexes for 'lines' text
    lines[i] = '* ' + lines[i] # add star to each string in the lines

text = '\n'.join(lines) 

pyperclip.copy(text) # copies the text to the clipboard

# Output - this is the program output

# * When this program is run, it replaces the text on the clipboard with 
# * text that has stars at the start of each line. Now the program is complete, and 
# * you can try running it with text copied to the clipboard.
# * Even if you don’t 