def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def get_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Contact not found."

def get_all_contacts(contacts):
    result = []
    if contacts:
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    else:
        return "No contacts found."