def isPhoneNumber(text):
    """
    checks whether the given text is a phone numner or not 
    """

    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = input("Type your text: ")
for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print("Phone Number found : " + chunk)

print("Thanks for using...")