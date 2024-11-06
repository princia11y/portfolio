class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ").lower()
        found_contacts = [contact for contact in self.contacts 
                          if search_term in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            print("\nSearch Results:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                contact.name = input(f"Enter new name ({contact.name}): ") or contact.name
                contact.phone = input(f"Enter new phone ({contact.phone}): ") or contact.phone
                contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
                contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                del self.contacts[index]
                print("Contact deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    manager = ContactManager()
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()