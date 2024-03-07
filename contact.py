import json

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f'Contact "{name}" added successfully.')

    def view_contact_list(self):
        if not self.contacts:
            print('Contact list is empty.')
        else:
            print('\nContact List:')
            for name, details in self.contacts.items():
                print(f'Name: {name}, Phone: {details["phone"]}')

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone']:
                results.append((name, details))
        return results

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f'Contact "{name}" updated successfully.')
        else:
            print(f'Contact "{name}" not found.')

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact "{name}" deleted successfully.')
        else:
            print(f'Contact "{name}" not found.')

    def save_to_file(self, filename='contact_book.json'):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print(f'Contact book saved to {filename}.')

    def load_from_file(self, filename='contact_book.json'):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print(f'Contact book loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found.')

def main():
    contact_book = ContactBook()

    while True:
        print('\nContact Book Menu:')
        print('1. Add Contact')
        print('2. View Contact List')
        print('3. Search Contact')
        print('4. Update Contact')
        print('5. Delete Contact')
        print('6. Save Contact Book')
        print('7. Load Contact Book')
        print('8. Exit')

        choice = input('Enter your choice (1-8): ')

        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email: ')
            address = input('Enter address: ')
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            keyword = input('Enter name or phone number to search: ')
            results = contact_book.search_contact(keyword)
            if results:
                print('\nSearch Results:')
                for name, details in results:
                    print(f'Name: {name}, Phone: {details["phone"]}')
            else:
                print('No matching contacts found.')

        elif choice == '4':
            name = input('Enter name of contact to update: ')
            phone = input('Enter new phone number: ')
            email = input('Enter new email: ')
            address = input('Enter new address: ')
            contact_book.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input('Enter name of contact to delete: ')
            contact_book.delete_contact(name)

        elif choice == '6':
            contact_book.save_to_file()

        elif choice == '7':
            contact_book.load_from_file()

        elif choice == '8':
            print('Exiting the Contact Book. Goodbye!')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 8.')

if __name__ == "__main__":
    main()
