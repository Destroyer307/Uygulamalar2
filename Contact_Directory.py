contacs = {}

def show_menu():
    print("\n --Contat Book Menu--")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name :")
    phone = input("Enter phone number :")
    email = input("Enter email :")
    contacs[name] = {"Phone":phone,"Email":email}
    print(f"{name} has been added to your contact book.")

def view_contact():
    if contacs:
        for name , details in contacs.items():
            print(f"name : {name}")
            print(f"Phone : {details['Phone']}")
            print(f"Email : {details['Email']}")
    else:
        print("Your contact book is empty.")

def search_contact():
    name = input("Enter the name of the contact you want to search : ")
    if name in contacs:
        print(f"Name : {name}")
        print(f"Phone {contacs[name]['Phone']}")
        print(f"Email : {contacs[name]['Email']}")
    else:
        print(f"Contact {name} not fount in your contact book.")

def edit_contact():
    name = input("Enter the name of the contact you want to edit :")
    if name in contacs:
        Phone = input("Enter new phone :")
        Email = input("Enter new email :")
        contacs[name] = {"Phone": Phone,"Email":Email}
        print(f"Contact {name} has been updated succesfully.")
    else:
        print(f"Contact {name} not found in your contact book.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete :")
    if name in contacs:
        del contacs[name]
        print(f"Contact {name} has been deleted succesfully.")
    else:
        print(f"Contact {name} not found in your contact book.")

while True:
    show_menu()
    choice = input("Enter your choice (1-6) : ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice please select a valid option (1-6)")
        