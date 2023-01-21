# # My Cat Name Program

# catNames = []
# while True:
#     print("Enter your cat name" + str(len(catNames) + 1) + "or type nothing to exit.:")
#     catName = input()
#     if catName == "":
#         break
#     catNames = catNames + [catName]

# Example Problem
import random

messages = ["It is certain",
"It is decidedly so",
"Yes definitely",
"Reply hazy try again",
"Ask again later",
"Concentrate and ask again",
"My reply is no",
"Outlook is not good",
"Very doubtful"]

print(messages[random.randint(1,9) - 1])