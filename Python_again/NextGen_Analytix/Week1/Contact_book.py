#2 Contact Book Using Python 

def contact_book():

    CONTACTS = {}

    enter_choice = 'y'

    def add_contact():
        print("\nADD A CONTACT:")
        name = input("Enter your name: ").strip().title()
        if name not in CONTACTS.keys():     
            try:
                phone = int(input("Enter your phone number: "))
                if phone > 0:
                    CONTACTS[name] = phone
                    return "Contact added successfully!\n"
                else:
                    return "Invalid number entered!\n"
            except ValueError:
                return "Invalid number entered!\n"
        else:
            return "Duplicate contacts!"

    def view_contacts():
        print("\nVIEW CONTACTS:")
        for name in CONTACTS.keys():
            print(f"{name} - {CONTACTS[name]}")
        return "All contacts fetched!\n" if CONTACTS else "No contacts yet!\n"

    def search_contact():
        print("\nSEARCH CONTACT:")
        search = input("Enter the name you want to search: ").strip().title()
        return f"Found: {search} - {CONTACTS[search]}\n" if search in CONTACTS.keys() else "Contact not found!\n"

    def update_contact():
        print("\nUPDATE CONTACT:")
        name = input("Enter the name you want to update: ").strip().title()
        if name in CONTACTS.keys():
            new_phone = int(input("Enter new phone number: "))
            CONTACTS[name] = new_phone
            return "Contact updated successfully!\n"
        else:
            return "No contact found!\n"
        
    def delete_contact():
        print("\nDELETE CONTACT:")
        name = input("Enter the contact you want to delete: ").strip().title()
        contact_exists = CONTACTS.pop(name, None)
        print("Contact doesn't exist!" if contact_exists == None else f"{name} contact has been deleted\n")
        return view_contacts()

    while enter_choice == 'y':

        print("\nMAIN MENU\n==================\n1. Add contact\n2. View contacts" \
            "\n3. Search contact\n4. Update contact\n5. Delete contact\n6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(add_contact())
                enter_choice = input("Do you want to continue (y/n)?: ")

            elif choice == 2:
                print(view_contacts()) if CONTACTS else print("\nEmpty contact book!\n")
                enter_choice = input("Do you want to continue (y/n)?: ")

            elif choice == 3:
                print(search_contact()) if CONTACTS else print("\nEmpty contact book!\n")
                enter_choice = input("Do you want to continue (y/n)?: ")

            elif choice == 4:
                print(update_contact()) if CONTACTS else print("\nEmpty contact book!\n")
                enter_choice = input("Do you want to continue (y/n)?: ")

            elif choice == 5:
                print(delete_contact()) if CONTACTS else print("\nEmpty contact book!\n")
                enter_choice = input("Do you want to continue (y/n)?: ")
            
            elif choice == 6:
                print("\nThank you for using Contact Book!")
                enter_choice = 'n'

            else:
                print("No operations exist for this choice!")

        except ValueError:
            print("Please enter a numerical choice.")

if __name__ == '__main__':
    contact_book()