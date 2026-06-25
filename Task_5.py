# ==========================================
# Task 5: Contact Book
#
# Objective:
# Create a contact management application
# that allows users to store and manage
# contact information.
#
# Features:
# - Add Contact
# - View Contacts
# - Search Contact
# - Update Contact
# - Delete Contact
# - User-Friendly Menu Interface
#
# ==========================================

# List to store all contacts
contacts = []


def add_contact():
    """Add a new contact."""
    print("\n--- Add New Contact ---")

    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    address = input("Enter Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("\nContact added successfully!")


def view_contacts():
    """Display all saved contacts."""
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")


def search_contact():
    """Search contact by name or phone number."""
    print("\n--- Search Contact ---")

    search_term = input(
        "Enter Name or Phone Number to search: "
    ).strip().lower()

    found = False

    for contact in contacts:
        if (
            search_term in contact["name"].lower()
            or search_term in contact["phone"]
        ):
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")


def update_contact():
    """Update existing contact details."""
    print("\n--- Update Contact ---")

    search_name = input(
        "Enter contact name to update: "
    ).strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:

            print("\nCurrent Contact Details:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")

            new_name = input(
                "Enter New Name (press Enter to keep current): "
            ).strip()

            new_phone = input(
                "Enter New Phone Number (press Enter to keep current): "
            ).strip()

            new_email = input(
                "Enter New Email (press Enter to keep current): "
            ).strip()

            new_address = input(
                "Enter New Address (press Enter to keep current): "
            ).strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("\nContact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    """Delete a contact."""
    print("\n--- Delete Contact ---")

    search_name = input(
        "Enter contact name to delete: "
    ).strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:

            print("\nContact Found:")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")

            confirm = input(
                "Are you sure you want to delete this contact? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                contacts.remove(contact)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Contact not found.")


def display_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("        CONTACT BOOK MENU")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 40)


# Main Program Loop
while True:
    display_menu()

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")