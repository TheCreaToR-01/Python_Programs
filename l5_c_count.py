import pprint

message = "It was a bright day in April, and the clocks were striking thirteen."

char_count = {}
for character in message:
    char_count.setdefault(character, 0)
    char_count[character] += 1

pprint.pprint(char_count) # it is for a cleaner display of the results of items of a dict