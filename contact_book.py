import os
import json
"""
The Python script provides functionality to manage a contact book by adding, deleting, displaying,
and searching contacts stored in a JSON file.

:param contact: The `contact` parameter is a dictionary containing the information of a contact to
be added to the contact book. The key of the dictionary is the name of the contact, and the value is
another dictionary containing the contact details such as phone number, email, address, etc
:return: The code provided returns messages based on the actions performed in the main function:
- When adding a contact, it returns either "Contact exists." if the contact being added already exists in the contact book, or "Contact has been added" if the contact is successfully added to the contact book and the file is updated with the new contact information.
- When displaying contacts, it returns the `contact_book`
"""

contact_book = {}
file = 'contact_book.json'

def add_to_contact_book(contact):
    """
    The function `add_to_contact_book` reads, updates, and writes contact information to a file in JSON
    format, ensuring no duplicate contacts are added.
    
    :param contact: The `contact` parameter is a dictionary containing the information of a contact to
    be added to the contact book. The key of the dictionary is the name of the contact, and the value is
    another dictionary containing the contact details such as phone number, email, address, etc
    :return: The function `add_to_contact_book` will return either "Contact exists." if the contact
    being added already exists in the contact book, or "Contact has been added" if the contact is
    successfully added to the contact book and the file is updated with the new contact information.
    """
    global contact_book 
    global file
    
    # Create the file if it doesn't exist
    if file not in os.listdir():
        open(file, 'x')
    
    # Read existing data from the file
    if os.path.getsize(file) == 0:
        with open(file, 'w') as f:
            f.write(json.dumps(contact_book))
    else:
        with open(file, 'r') as f:
            data = f.read()
            contact_book = json.loads(data)

    # Extract the contact name
    contact_name = list(contact.keys())[0]
    
    # Check if the contact already exists
    if contact_name in contact_book:
        return "Contact exists."
    
    # Update the contact book
    contact_book.update(contact)

    # Write the updated data back to the file
    with open(file, 'w') as f:
        f.write(json.dumps(contact_book, indent=4))

    return "Contact has been added"



def add_contact():
    """
    The `add_contact` function prompts the user to enter a person's first name, last name, and phone
    number, creates a contact entry, and then adds it to a contact book.
    """
    contact_first_name = input("Enter the person's first name:\n")
    contact_last_name = input("Enter the person's last name:\n")
    contact_name = contact_first_name +"_"+ contact_last_name
    contact_phone_no = input("Enter contact phone number:\n")
    contact_to_add = {contact_name: {
            "First_Name": contact_first_name, 
            "Last_Name": contact_last_name, 
            "Phone_Number": contact_phone_no
        }
    }
    print(f"Adding to contact book")
    print(add_to_contact_book(contact_to_add))
    


def display_contacts():
    """
    The `display_contacts` function reads contact data from a file and returns it as a dictionary.
    :return: The function `display_contacts()` is returning the `contact_book` dictionary after reading
    and loading the data from the file specified by the `file` variable.
    """
    global contact_book
    global file
    with open(file, 'r') as f:
        data = f.read()
        contact_book = json.loads(data)
    return contact_book
    


def search_contact(contactname):
    """
    The function `search_contact` reads contact data from a file, searches for a contact by name in the
    contact book, and returns the contact details if found.
    
    :param contactname: The `search_contact` function takes a `contactname` parameter as input. This
    parameter is used to search for a contact in the `contact_book` based on the first name or last name
    of the contact
    :return: The `search_contact` function is returning either a list of found contacts that match the
    specified name, or a message stating that the contact was not found.
    """
    global contact_book
    global file
    
    # Read existing data from the file
    with open(file, 'r') as f:
        data = f.read()
        contact_book = json.loads(data)
    
    # Search for the contact with the specified name
    found_contacts = [contact_book.get(contact_name, {}) for contact_name, details in contact_book.items() if contactname in details.get("First_Name", "") or contactname in details.get("Last_Name", "")]

    # Check if any contacts were found
    if found_contacts:
        return found_contacts
    else:
        return f"Contact '{contactname}' not found."


def delete_contact(contactname):
    """
    The `delete_contact` function deletes a contact from a contact book stored in a file based on the
    specified first name.
    
    :param contactname: The `delete_contact` function takes a `contactname` parameter, which is the
    first name of the contact that you want to delete from the contact book. The function searches for a
    contact with the specified first name in the contact book and deletes it if found. If the contact is
    successfully deleted,
    :return: The function `delete_contact(contactname)` returns a message indicating whether the contact
    with the specified first name was successfully deleted or not. If the contact is found and deleted,
    it returns "Contact '{contactname}' has been deleted.". If the contact is not found in the contact
    book, it returns "Contact '{contactname}' not found.".
    """
    global contact_book
    global file
    
    # Read existing data from the file
    with open(file, 'r') as f:
        data = f.read()
        contact_book = json.loads(data)
    
    # Search for the contact with the specified first name
    for contact_key, details in contact_book.items():
        if details.get("First_Name") == contactname:
            del contact_book[contact_key]
            # Write the updated data back to the file
            with open(file, 'w') as f:
                f.write(json.dumps(contact_book, indent=4))
            return f"Contact '{contactname}' has been deleted."
    
    # If contact not found
    return f"Contact '{contactname}' not found."


def main():
    """
    The main function allows users to add, delete, display, search contacts in an address book using
    different commands.
    """
    print("Add a contact to your address book:\n")
    while True:
        print("\nEnter 'A' to Add to contacts")
        print("Enter 'Del' to delete contact")
        print("Enter 'd' to display the contacts")
        print("Enter 's' to search the contacts")
        print("Enter 'q' to quit")
        message = input("\nEnter an option to continue:\n")
          
        if message.lower() == 'a':
            add_contact()
        elif message.lower() == 'd':
            print(display_contacts())
        elif message.lower() == 's':
            print(search_contact(input("Enter a contact to search for:\n")))
        elif message.lower() == "del":
            print(delete_contact(input("Enter the contact to delete:\n")))
        elif message.lower() == 'q':
            break
        else:
            print("Invalid entry. Please try again.")


if __name__ == "__main__":
    main()
        
