import os
os.system("cls")

acc = {}

def register():
    os.system("cls")
    data = open("data.txt", "a")
    word = open("pass.txt", "a")

    user = input("Username: ")
    password = input("Password: ")

    if user in open("data.txt").read():
        print("Username already exists!")
    else: 
        print(f"Username: {user}", file=data)
        print(f"Password: {password}", file=word)
        print("You've successfully created your account!")

def login():
    os.system("cls")
    user = input("Username: ")
    password = input("Password: ")
    data = open("data.txt", "r") 
    word = open("pass.txt", "r")
    users = [line.strip() for line in data]
    passwords = [line.strip() for line in word]

    if user in users:
        index = users.index(user)
        if password == passwords[index]:
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("User not found!")

def change():
    os.system("cls")
    user = input("Username: ")
    old_password = input("Enter old Password: ")

    data = open("data.txt", "r")
    word = open("pass.txt", "r")
    users = [line.strip() for line in data]
    passwords = [line.strip() for line in word]

    if user in users:
        index = users.index(user)
        if old_password == passwords[index]:
            new_password = input("Enter new Password: ")
            confirm_password = input("Confirm new Password: ")
            if new_password == confirm_password:
                passwords[index] = new_password
                with open("pass.txt", "w") as word:
                    word.write("\n".join(passwords) + '\n')
                print("Password changed successfully!")
            else:
                print("New passwords do not match!")
        else:
            print("Old password incorrect!")
    else:
        print("User not found!")

while True:
    print("1 - Register \n2 - Login \n3 - Change Password \n4 - Exit")
    choice = int(input("Enter a Choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        change()
    elif choice == 4:
        break
    else:
        print("Invalid Choice.")