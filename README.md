# pp-1-password_manager
This is a password manager built by using python and encryption and decryption using cryptography module and tools (updates  will be pushed gradually with time)
# 🔐 Password Manager

A simple **Python-based password manager** that securely stores passwords using **Fernet symmetric encryption** from the `cryptography` library.

This project was built to understand the basics of **Python file handling, encryption, decryption, functions, and password security**.

## ✨ Features

* 🔒 Encrypts passwords using **Fernet encryption**
* 🔑 Uses a separate encryption key
* 💾 Stores encrypted passwords in a text file
* 🔓 Decrypts passwords only when viewing them
* ➕ Add new account credentials
* 👀 View saved credentials
* 🐍 Built completely with Python
* 📁 Uses simple local files for storage

## 🛠️ Technologies Used

* **Python**
* **Cryptography**
* **Fernet Encryption**
* **File Handling**
* **Functions**

## 📦 Installation

First, install the required library:

```bash
pip install cryptography
```

Then clone the repository:

```bash
git clone https://github.com/your-username/password-manager.git
```

Move into the project folder:

```bash
cd password-manager
```

Run the program:

```bash
python main.py
```

## 🔐 How Encryption Works

The project uses **Fernet**, which provides authenticated symmetric encryption.

The basic process is:

```text
Password
   ↓
Fernet Encryption
   ↓
Encrypted Password
   ↓
Stored in passwords.txt
```

When viewing the password:

```text
Encrypted Password
   ↓
Fernet Decryption
   ↓
Original Password
```

The encryption key is stored separately in:

```text
security.key
```

## 📁 Project Structure

```text
Password-Manager/
│
├── main.py
├── security.key
├── passwords.txt
├── master_password.txt
└── README.md
```

### `main.py`

Contains the main Python program, including functions for adding and viewing passwords.

### `security.key`

Contains the Fernet encryption key used to encrypt and decrypt passwords.

### `passwords.txt`

Stores account names along with their **encrypted passwords**.

### `master_password.txt`

Stores the encrypted master-password information used to control access to the password manager.

## 🔄 Basic Workflow

### 1. Add Password

The user enters:

```text
Account → Password
```

The password is then encrypted before being stored.

### 2. Store Password

Instead of storing:

```text
Google|mypassword123
```

the program stores something similar to:

```text
Google|gAAAAAB...
```

So the actual password is not directly visible in the file.

### 3. View Password

When the user requests a saved password:

```text
Encrypted Password
        ↓
     Decrypt
        ↓
  Original Password
```

## ⚠️ Important Security Notes

This is an **educational project**, not a production-ready password manager.

Some limitations include:

* The encryption key is stored locally.
* The password database is stored in a normal text file.
* There is no secure database system.
* There is no multi-factor authentication.
* The master-password system could be improved.
* Anyone who obtains both the password database **and encryption key** may be able to decrypt the stored passwords.
* File permissions and operating-system security are not handled by the project.

**Never use this project to store important real-world passwords unless you understand and improve its security.**

## 🚀 Future Improvements

Possible upgrades:

* [ ] Add a proper GUI using Tkinter
* [ ] Add a secure master-password system
* [ ] Add password generation
* [ ] Add password search
* [ ] Add edit/delete functionality
* [ ] Use SQLite instead of text files
* [ ] Improve key management
* [ ] Add automatic password-strength checking
* [ ] Add clipboard support
* [ ] Add better error handling
* [ ] Add unit tests

## 🎯 Learning Goals

This project helped me practice:

* Python functions
* `input()` and user interaction
* File handling with `open()`
* Reading and writing files
* String and bytes conversion
* Encryption and decryption
* Python modules
* Exception handling
* Basic cybersecurity concepts

## 👨‍💻 Author

**Chanpreet Singh**

Built as a Python learning project to explore **cryptography and cybersecurity fundamentals**.

---

⭐ If you found this project interesting, feel free to check out the code and suggest improvements!


