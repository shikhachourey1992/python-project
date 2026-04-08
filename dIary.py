# Create a Student Diary App
# Features:
# Add daily diary entry
# Read all diary entries
# Search diary by date
#
# Add "Delete All Notes" option
# Add menu option 5. Delete all notes that clears the file by writing an empty string.

while True:
 print("Add diary entry")
 print("Read all entries")
 print("Search diary by date")
 print("exit")
 choice=input("enter your choice: ")
 if choice=="1":
    entry=input("enter your entry:")
    date=input("enter your date")
    with open("daiary.txt","a")as file:
      file.write(entry)
      print(entry,date)
 elif choice=="2":
    with open("daiary.txt","r")as file:
      print(file.read())
 elif choice=="3":
     date=input("search date:")
     with open("daiary.txt","r")as file:
      print(entry,date)
 elif choice=="4":
    print("exit")
    break
 else:
     print("invalid choice")









