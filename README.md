# pp-1-password_manager
This is a password manager built by using python and encryption and decryption using cryptography module and tools (updates  will be pushed gradually with time)
                 ┌──────────────────────┐
                 │       START          │
                 └──────────┬───────────┘
                            │
                            ▼
              ┌──────────────────────────┐
              │ Read security.key        │
              │ from the file            │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Create Fernet object     │
              │ fernet = Fernet(key)     │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Ask for master password  │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Read encrypted master    │
              │ password from file       │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Decrypt master password  │
              └────────────┬─────────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Password correct? │
                 └───────┬─────┬─────┘
                         │YES  │NO
                         │     │
                         ▼     ▼
                  ┌─────────┐ ┌──────────────┐
                  │  MENU   │ │ Print error  │
                  └────┬────┘ │    + quit    │
                       │      └──────────────┘
             ┌─────────┼─────────┐
             │         │         │
             ▼         ▼         ▼
           ADD       VIEW       QUIT
             │         │         │
             ▼         ▼         ▼
        Encrypt     Read file   EXIT
        password    ↓
             │      Decrypt
             ▼      passwords
        Save to
        file
             │         │
             └────┬────┘
                  │
                  ▼
               MENU AGAIN

