#my code
class Addcontact():
    def contact(self):
        self.name=input('Enter name: ')
        self.phno=int(input('Enter phno: '))
        self.mailid=input('Enter mailid: ')
        print(f'Name: {self.name}')
        print(f'Phno: {self.phno}')
        print(f'MailID: {self.mailid}')
        print('Contact added successfully')
class Updatecont(Addcontact):
    def update(self):
        self.change=input('Enter the name of contact to be updated: ')
        if self.change==self.name:
            self.oldphno=int(input('Enter old phno: '))
            if self.oldphno==self.phno:
                self.newphno=int(input('Enter new phno: '))
            else:
                print('Old phno doesnot match')
        else:
            print('No existing name in contacts')
        print(f'Name: {self.name}')
        print(f'Phno: {self.phno}')
        print(f'MailID: {self.mailid}')
class ListofContacts(Updatecont):
    def display(self):
        print('Contact List')
        print(f'Name: {self.name}')
        print(f'Phno: {self.phno}')
        print(f'MailID: {self.mailid}')
class Removecont(ListofContacts):
    def removal(self):
        self.delete=input('Enter contact name to be deleted: ')
        if self.delete==self.name:
            self.name=''
            self.phno=''
            self.mailid=''
            print(f'Name: {self.name}')
            print(f'Phno: {self.phno}')
            print(f'MailID: {self.mailid}')
            print('Contact deleted')
        else:
            print('No existing contact')
a=Removecont()
while True:
    choice=input('''Choose an option:
                    1.Add contact
                    2.Update contact
                    3.List of contacts
                    4.Remove contact
                    5.Exit
                    ''')
    if choice=='1':
        a.contact()
    elif choice=='2':
        a.update()
    elif choice=='3':
        a.display()
    elif choice=='4':
        a.removal()
    elif choice=='5':
        print('Existing...')
        break
    else:
        print('Invalid choice')


#code-2
'''
contacts = []

while True:
    print("\nCONTACT BASE MANAGEMENT SYSTEM")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Remove Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        mobile = input("Enter mobile number: ")
        mail = input("Enter mail id: ")

        contacts.append({
            "name": name,
            "mobile": mobile,
            "mail": mail
        })

        print("Contact added successfully!")

    elif choice == "2":
        old_mobile = input("Enter old mobile number: ")
        found = False

        for contact in contacts:
            if contact["mobile"] == old_mobile:
                new_mobile = input("Enter new mobile number: ")
                contact["mobile"] = new_mobile
                found = True
                print("Contact updated successfully!")
                break

        if not found:
            print("Contact not found!")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nList of Contacts:")
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print("Name:", contact["name"])
                print("Mobile:", contact["mobile"])
                print("Mail ID:", contact["mail"])

    elif choice == "4":
        mobile = input("Enter mobile number to remove: ")
        found = False

        for contact in contacts:
            if contact["mobile"] == mobile:
                contacts.remove(contact)
                found = True
                print("Contact removed successfully!")
                break

        if not found:
            print("Contact not found!")

    elif choice == "5":
        print("Exiting Contact App...")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")



#code-3

class Contact:
    def __init__(self, name, mobile, mail):
        self.name = name
        self.mobile = mobile
        self.mail = mail


class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile number: ")
        mail = input("Enter mail id: ")

        contact = Contact(name, mobile, mail)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def update_contact(self):
        old_mobile = input("Enter old mobile number: ")

        for contact in self.contacts:
            if contact.mobile == old_mobile:
                new_mobile = input("Enter new mobile number: ")
                contact.mobile = new_mobile
                print("Contact updated successfully!")
                return

        print("Contact not found!")

    def list_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts available.")
        else:
            print("\nList of Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {i}")
                print("Name:", contact.name)
                print("Mobile:", contact.mobile)
                print("Mail ID:", contact.mail)

    def remove_contact(self):
        mobile = input("Enter mobile number to remove: ")

        for contact in self.contacts:
            if contact.mobile == mobile:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return

        print("Contact not found!")

    def menu(self):
        while True:
            print("\nCONTACT BASE MANAGEMENT SYSTEM")
            print("1. Add Contact")
            print("2. Update Contact")
            print("3. List Contacts")
            print("4. Remove Contact")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.update_contact()
            elif choice == "3":
                self.list_contacts()
            elif choice == "4":
                self.remove_contact()
            elif choice == "5":
                print("Exiting Contact App...")
                break
            else:
                print("Invalid choice! Please enter 1 to 5.")


app = ContactManagementSystem()
app.menu()
'''
