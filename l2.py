# # # # from unicodedata import name


# # # # name = input("What is your name?")
# # # # if name == "Kushagra Dubey":
# # # #     print("Welcome Kushagra")
# # # # elif name == "Dubey":
# # # #     print("Only your sirname is same.")
# # # # else:
# # # #     print("You aren't Kushagra, kiddo!")

# # # while True:
# # #     print("What is your name?")
# # #     name = input()
# # #     if name != "Kushagra":
# # #         continue
# # #     print("Hello Kushagra. What is the password? (It is a fish)")
# # #     password = input()
# # #     if password == "swordfish":
# # #         break
# # # print("Access Granted.")


# # # Truthy and Falsey Values
# # # 0, 0.0, "" are considered as False
# # # else are considered as True

# # name = ""
# # while not name:
# #     print("Enter your name:")
# #     name = input()
# # print("How many guests will you have?")
# # numOfGuests = int(input())
# # if numOfGuests:
# #     print("Be sure to have enough tea for the guests.")
# # print("Done")

# print("My name is")
# for i in range(5):
#     print("Kushagra " + str(i))
#     i +=1


import sys

while not False:
    print("Type exit to quit")
    response = input()

    if response== 'exit' :
        sys.exit()
    print("You typed " + response + ".")