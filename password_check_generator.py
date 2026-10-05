def check_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        strength -= 1
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        strength -= 1
        print("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password): 
        strength += 1
    else:
        strength -= 1
        print("Password should contain at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        strength -= 1
        print("Password should contain at least one digit.")

    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        strength += 1
    else:
        strength -= 1
        print("Password should contain at least one special character.")
    

    # Evaluate strength
    if strength >= 4:
        print("Your password is strong.")
    elif strength >= 3:
        print("Your password is moderate.")
    else:
        print("Your password is weak.")
    return strength

def generate_password(length=12, include_symbols=True):
    from random import choice as ch
    import string
    
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    else:
        characters = string.ascii_letters + string.digits
        if include_symbols:
            characters += "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        
        password = " ".join(ch(characters) for i in range(length))
        return password

def main():
    print("--------Password Strength Checker and Generator--------")
    while True:
        print("\nMenu:")
        print("1. Check Password Strength")
        print("2. Generate Password")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Please enter integers only!")
            continue
        
        if choice == 1:
            password = input("Enter your password: ")
            check_strength(password)
        elif choice == 2:
            length = int(input("Enter desired password length (minimum 8): "))
            include_symbols = input("Include special characters? (y/n): ").lower() == 'y'
            password = generate_password(length, include_symbols)
            if password:
                print(f"Generated Password: {password}")
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
