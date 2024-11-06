import random
import string

def display_instructions():
    print("\n--- Welcome to the Password Generator ---")
    print("Instructions:")
    print("1. Enter the desired password length.")
    print("2. Choose whether to include uppercase letters, lowercase letters, digits, and/or symbols.")
    print("3. Your generated password will be displayed.")
    print("4. Type 'q' to quit.\n")

def get_user_preferences():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, include_uppercase, include_lowercase, include_digits, include_symbols

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
    # Create the character pool based on user preferences
    character_pool = ''
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    # Ensure there are characters to select from
    if not character_pool:
        return "Error: No character types selected. Please try again."

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def display_password(password):
    print(f"\nGenerated Password: {password}\n")

def main():
    display_instructions()
    
    while True:
        user_input = input("Press 'g' to generate a new password or 'q' to quit: ").lower()
        if user_input == 'q':
            print("Thank you for using the Password Generator. Goodbye!")
            break
        elif user_input == 'g':
            length, include_uppercase, include_lowercase, include_digits, include_symbols = get_user_preferences()
            password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
            display_password(password)
        else:
            print("Invalid input. Please enter 'g' to generate or 'q' to quit.")

# Start the program
main()
