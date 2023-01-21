def comma_code(num):
    for i in range(len(num) - 1):
        print(num[i] + ',', end = ' ')

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)
print(' and ' + spam[-1])