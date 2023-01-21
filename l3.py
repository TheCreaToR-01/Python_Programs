# # def hello(name):
# #     print(f"""Hello
# #     {name}, How are you?
# #     Hope you are doing well.""")

# # hello("Nilesh")
# # hello("Kartikey")
# # hello("Akansha")
# # hello("Dinmay")
# # hello("Karna")
# # hello("Arjuna")
# # hello("Kanha")

# import random

# def astro(answerNumber):
#     if answerNumber == 1:
#         return "It is certain"
#     elif answerNumber == 2:
#         return "It is decidedly so"
#     elif answerNumber == 3:
#         return "Yes"
#     elif answerNumber == 4:
#         return "Reply hazy try again"
#     elif answerNumber == 5:
#         return "Ask again later"
#     elif answerNumber == 6:
#         return "Concentrate and ask again"
#     elif answerNumber == 7:
#         return "My reply is no"

# r = random.randint(1,7)
# fortune = astro(r)
# print(fortune)

#Number _ Guessing _ Game

import random
print("I am thinking of a number between 1 to 20")
guessCount = 0
secret_code = random.randint(1,20)
while guessCount <=5:
    guess = int(input("Take a guess:"))
    if guess > secret_code:
        print("Your guess is too high.")
    elif guess < secret_code:
        print("Your guess is too low.")
    else:
        break
    guessCount += 1
if guess == secret_code:
    print("""Good job! You guessed the right number in """ + str(guessCount) + ' guesses. Nice to play with you.')
else:
    print("No, I was thinking of " + str(secret_code))
    

