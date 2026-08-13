from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# with open("security.key","wb") as key_file:
#     key_file.write(key)

def add_pwd():
    name = input("Account number: ")
    pwd = input("Password: ")
    encrypted_pwd = fernet.encrypt(pwd.encode())
    with open("passwords.txt" , "a") as f:
        f.write(name + "|" + encrypted_pwd.decode() + "\n")



def view_pwd():
    with open("passwords.txt" , "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"username: {user} password: {fernet.decrypt(passw.encode()).decode()}")

with open("security.key","rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)


# set_master_pwd = input("Set master password to gain acess: ")
# set_master_pwd = fernet.encrypt(set_master_pwd.encode())
# with open("master_password.txt" , "a") as master_pwd_file:
#     master_pwd_file.write(set_master_pwd.decode())

master_pwd = input("Enter master password to gain access: ")

with open("master_password.txt", "r") as master_pwd_file:
    encrypted_master_pwd = master_pwd_file.read()


master_pwd_real = fernet.decrypt(encrypted_master_pwd.encode()).decode()

if master_pwd_real != master_pwd:
        print("Incorrect master password")
        quit()


while True:

    mode = input("Select the mode to continue (add,view) passwords or you can choose (quit): ")
    if mode=="quit":
        quit()
    if mode=="add":
        add_pwd()
    elif mode=="view":
        view_pwd()
    else:
        print("invalid mode choosen!")
        continue