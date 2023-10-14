def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:    
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        return 'Wrong syntax!'

def change_phone(args, contacts):
    try:    
        name = args[0]
        phone = args[1]
        if name in contacts:
            contacts[name] = phone
            return f'Success! Phone number for {name} changed to {phone}'
        else:
            return f'Error! There is no {name} in the contact list'
    except:
        return 'Wrong syntax!'
            
def return_phone(args, contacts):
    try:    
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f'There is no {name} in the contact list'
    except:
        return 'Wrong syntax!'

def all(contacts):
    contact_list = ''
    for contact in contacts:
        contact_list += f'{contact}: {contacts[contact]}\n'
    return contact_list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_phone(args, contacts))
        elif command == 'phone':
            print(return_phone(args, contacts))
        elif command == 'all':
            print(all(contacts))
        else:
            print("Invalid command.")


main()