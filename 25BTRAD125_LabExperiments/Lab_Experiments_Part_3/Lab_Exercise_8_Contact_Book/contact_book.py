print("========== CONTACT BOOK ==========")

contacts = {}


def show_contact(name):
    contact = contacts[name]
    print("-" * 45)
    print(f"  Name  : {name}")
    print(f"  Phone : {contact['phone']}")
    print(f"  Email : {contact['email']}")
    print(f"  City  : {contact['city']}")
    print("-" * 45)


def add_contact():
    name = input("Enter contact name: ").strip().title()
    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print(f"Contact '{name}' already exists. Use the update option.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! It must contain exactly 10 digits.")
        return

    email = input("Enter email address: ").strip()
    if "@" not in email or "." not in email:
        print("Invalid email address!")
        return

    city = input("Enter city: ").strip()
    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city if city else "Not provided",
    }
    print(f"Contact '{name}' added successfully.")


def search_contact():
    query = input("Enter name to search: ").strip().title()
    if not query:
        print("Search text cannot be empty!")
        return

    if query in contacts:
        show_contact(query)
        return

    matches = [name for name in contacts if query in name]
    if matches:
        print(f"Found {len(matches)} matching contact(s):")
        for name in sorted(matches):
            show_contact(name)
    else:
        print("No contact found with that name.")


def update_contact():
    name = input("Enter name to update: ").strip().title()
    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave a field blank to keep the old value.")
    phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New email [{contacts[name]['email']}]: ").strip()
    city = input(f"New city [{contacts[name]['city']}]: ").strip()

    if phone:
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number! Update cancelled.")
            return
        contacts[name]["phone"] = phone

    if email:
        if "@" not in email or "." not in email:
            print("Invalid email address! Update cancelled.")
            return
        contacts[name]["email"] = email

    if city:
        contacts[name]["city"] = city

    print(f"Contact '{name}' updated successfully.")


def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input(f"Delete contact '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Delete cancelled.")


def display_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return

    print("\n" + "=" * 75)
    print("CONTACT LIST")
    print("=" * 75)
    print(f"{'Name':<20} {'Phone':<14} {'Email':<25} {'City':<12}")
    print("-" * 75)
    for name in sorted(contacts):
        contact = contacts[name]
        print(
            f"{name:<20} {contact['phone']:<14} "
            f"{contact['email']:<25} {contact['city']:<12}"
        )
    print("=" * 75)
    print(f"Total contacts: {len(contacts)}")


while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
