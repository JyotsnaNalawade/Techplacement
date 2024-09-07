contacts={}

while True:
    print("\nContact Menu:")
    print("1. Add Contacts")
    print("2. Delete Contacts")
    print("3. Upadate Contacts")
    print("4. Search Contacts")
    print("5. Display Contacts")
    print("6. Exit")
    
    def add_contact():
        name = input("Enter name: ")
        phone = input("Enter a phone number: ")
        if name in contacts:
            print("This contact already exists.")
        else:
            contacts[name] = phone
            print("\ncontact have been added successfully")
            
    def update_contact():
        name = input("Enter name: ")
        for contact in contacts:
            if contact==name:
                phone = input("Enter the new phone number: ")
                contacts[name]=phone
                print("contact updated successfully.")
                break
            else:
                print("This contact does not exist")
                
    def search_contact():
        name = input("Enter name: ")
        for contact in contacts:
            if contact.lower()== name.lower():
                print("Contact Found")
                print(contact,contacts[contact])  
                break
            else:
                print("contact not found")
                
    def display_contact():
        if contacts=={}:
            print("There are no contacts")
        else:
            print("Contact List:")
            for name, phone in contacts.items():
                print(name, phone)
                       
    def delete_contact():
        name = input("Enter a name: ")
        if name in contacts:
            del contacts[name]
            
        
            
                
    choice=int(input("Enter your Choice (1-6): "))
    
    if choice == 1:
        add_contact()
        
    elif choice == 2:
        delete_contact()
        
    elif choice == 3:
        update_contact()
        
    elif choice == 4:
        search_contact()
        
    elif choice == 5:
        display_contact()
        
    elif choice == 6:
        print("Existing the contactbook. bye")
        
    else:
        print("Invalid choice. please enter number between 1 to 6.")