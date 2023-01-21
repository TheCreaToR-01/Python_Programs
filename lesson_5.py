# Dictionaries Intro

dict1 = {'name':'Kushagra', 'qualification':'Graduate', 'work':'Google'}

# print(f"My name is {dict1['name']}. I am {dict1['qualification']} and work at {dict1['work']}.")

# print(dict1.values())

# for v in dict1.values(): # to iterate over values
#     print(v)

# for k in dict1.keys(): #iterating over the keys
#     print(k)

for i in dict1.items(): #iterates over both keys and values
    print(list(i))

for k, v in dict1.items():
    print("Key:" + k + ' Value:' + v)

print('name' in dict1) #checking whether the key is in dict or not

print(f"My name is {dict1['name']}. I am a {dict1['qualification']}. I work at {dict1['work']} and an ex-employee of {dict1.get('ex-work', 'Amazon')}.")

#get(key, default value(uses if key is not in the dictionary)) func usage in the dict, checks whether the keys in dict and if not then uses its default value)

# if 'age' not in dict1:
#     dict1['age'] = 22

dict1.setdefault('age', 22) # it is similar to the get function, checks the key first and then adds it with value if not found
print(dict1['age'])