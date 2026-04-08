contact={}
while True:
    print("1.Add contact")
    print("2.view contact")
    print("3. search contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name=input("Enter your name: ")
        phone=input("Enter your phone number: ")
        contact[name]=phone
        print("Contact added")
    elif choice == "2":
        print("Contact list")
        for name,phone in contact.items():
            print(name,":",phone)
    elif choice == "3":
        search=input("Enter search name ")
        if search in contact:
            print(search,":",contact[search])
        else:
            print("Contact not found")
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid choice")

