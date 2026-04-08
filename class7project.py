friends=[]
while True:
    print("--Friend list manager--")
    print("1. Add friend")
    print("2. Remove friend")
    print("3. veiw all friends")
    print("4. Exit")

    choice=input("Enter your choice")
    if choice=="1":
       name=input("Enter your friend's name")
       friends.append(name)
       print(name,"added")
    elif choice=="2":
        name = input("Enter your friend's name")
        if name in friends:
          friends.remove(name)
          print(name, "removed")
        else:
            print("Sorry, no friend")
    elif choice == "3":
        print(friends)
    elif choice == "4":
        print("Exit")
        break
    else:
        print("invalid choice")






