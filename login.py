# login.py
def login(username, password):
    """
    Simple login function that checks credentials
    Returns True if login is successful, False otherwise
    """
    # Example credentials (don’t use this in real apps—it’s not secure!)
    valid_credentials = {
        "user1": "password123",
        "admin": "admin456"
    }
    
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    return False

# Test the function
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    if login(user, pwd):
        print("Login successful!")
    else:
        print("Invalid credentials")
