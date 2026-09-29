
import json

my_contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(my_contacts, file)

def load_contacts():
    global my_contacts
    try:
        with open("contacts.json", "r") as file:
            my_contacts = json.load(file)
    except FileNotFoundError:
        my_contacts = {}

load_contacts()

while True:
    print("\n" + "=" * 40)
    print("            CONTACT BOOK")
    print("=" * 40)
    
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        my_contacts[name] = {
            "phone": phone,
            "email": email
        }

        save_contacts()
        print("Contact Added Successfully!")

    elif choice == "2":
        if not my_contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for name, info in my_contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("-" * 20)

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in my_contacts:
            print("\nContact Found:")
            print("Phone:", my_contacts[search]["phone"])
            print("Email:", my_contacts[search]["email"])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete = input("Enter name to delete: ")

        if delete in my_contacts:
            del my_contacts[delete]
            save_contacts()
            print("Contact Deleted Successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book.")
        print("All contacts have been saved successfully!")
        break

    else:
        print("Invalid choice. Try again.")