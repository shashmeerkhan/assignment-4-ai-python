from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Checks if the provided email and password match the stored logins.
    Returns True if login is successful, otherwise False.
    """
    hashed_password = hash_password(password_to_check)

    # Check if email exists in the dictionary
    if email in stored_logins:
        if stored_logins[email] == hashed_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("Email not found.")
        return False


def hash_password(password):
    """
    Hashes the given password using SHA256.
    """
    return sha256(password.encode()).hexdigest()


def main():
    # Dictionary containing stored email-password pairs (hashed passwords)
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }

    # Test cases
    login("example@gmail.com", stored_logins, "word")          # Incorrect password
    login("example@gmail.com", stored_logins, "password")      # Correct password

    login("code_in_placer@cip.org", stored_logins, "Karel")    # Correct password
    login("code_in_placer@cip.org", stored_logins, "karel")    # Incorrect password

    login("student@stanford.edu", stored_logins, "password")   # Incorrect password
    login("student@stanford.edu", stored_logins, "123!456?789") # Correct password

    login("unknown@example.com", stored_logins, "test")        # Email not found


if __name__ == '__main__':
    main()
