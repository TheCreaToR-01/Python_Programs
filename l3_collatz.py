#Practice Problem - Collatz Function()

# def collatz(number):
#     if number % 2 == 0:
#         res_1 = number // 2
#         if res_1 != 1:
#             print(res_1)
#             collatz(res_1)
#         else:
#             print(1)
#     elif number % 2 == 1:
#         res_2 = 3 * number + 1
#         if res_2 != 1:
#             print(res_2)
#             collatz(res_2)
#         else:
#             print(1)
#     else:
#         return 1


# Alternate Method

# inp_num = int(input('Enter a number:\n'))
# collatz(inp_num)



from multiprocessing.sharedctypes import Value


try:
    number = int(input("Enter a number:\n"))
    while number > 1:
        if number % 2 == 0:
            number = int(number) // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * int(number) + 1
            print (number)
        else:
            break
except ValueError:
    print("Enter an integer.")