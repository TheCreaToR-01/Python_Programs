# Birthday Remember Program
birthdays = {'Neelesh': 'Nov 19', 'Kushagra': 'July 6', 'Shivam': 'Nov 14', 'Nitesh': 'August 25', 'Dhruv': 'Jan 6', 'Aradhya': 'Aug 14'}

while True:
    name = input("Enter the name(blank to quit):")

    if name == "":
        break

    elif name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}.')
    else:
        print(f"I do not have birthday information for {name}.")
        b_day = input("What is the birthday?")
        birthdays[name] = b_day
        print('Birthday data successfully updated.')