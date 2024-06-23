class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.\n")
            return
        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone}")
        print("")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                self.display_contact(contact)
        else:
            print("No contacts found matching the search term.\n")

    def update_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            print("Enter new details (leave blank to keep current value):")
            new_phone = input(f"Phone ({contact.phone}): ") or contact.phone
            new_email = input(f"Email ({contact.email}): ") or contact.email
            new_address = input(f"Address ({contact.address}): ") or contact.address
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address
            print(f"Contact for {name} updated successfully.\n")
        else:
            print(f"No contact found for name: {name}\n")

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact for {name} deleted successfully.\n")
        else:
            print(f"No contact found for name: {name}\n")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}\n")

def main():
    manager = ContactManager()

    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone to search: ")
            manager.search_contact(search_term)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            manager.update_contact(name)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()