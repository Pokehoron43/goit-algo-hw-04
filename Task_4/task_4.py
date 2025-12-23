def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def command_phone(name,contacts):
    return contacts.get(name)

def command_change(new_phone, name, contacts):
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return "Contact not found."

def command_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

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
        elif command == "change":
            if len(args) != 2:
                print("Usage: change <name> <new_phone>")
                continue
            name, new_phone = args
            print(command_change(name, new_phone, contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone <name>")
                continue
            name = args[0]
            print(command_phone(name, contacts))
        elif command == "all":
            print(command_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
