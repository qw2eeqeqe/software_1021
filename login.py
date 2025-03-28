# login.py
def login(username, password):
    """
    Simple login function that checks credentials
    Returns True if login is successful, False otherwise
    """

        "user1": "password123",
        "admin": "admin456"
    }
    
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    return False

if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    if login(user, pwd):
        print("Login successful!")
    else:
        print("Invalid credentials")
