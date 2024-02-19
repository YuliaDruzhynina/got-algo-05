def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter user name"
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
                

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split() #создали переменные для команды и контактов в строк инпут
    cmd = cmd.strip().lower()#рядок команда убрали все пробелы по краям 
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args #создали переменные из списка arg
    contacts[name] = phone#создали ключ-значение в словарь
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contact(args, contacts)
    else:
        "Contact added."

@input_error
def show_phone(args,contacts):     
    return contacts[args[0]]#если есть в словаре ключ-имя вернуть его значение-номер

@input_error
def show_all(args,contacts):
    s=''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]}\n")
    return s

def main():
    contacts = {}
    print("Welcome to the assistant bot! Ulyana!")
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
            print(add_contact(args, contacts))
        elif command == "show":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(args,contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
