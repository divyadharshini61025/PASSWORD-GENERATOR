import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for good security.")
        return ""

    # Create a combined list of all characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one lowercase, one uppercase, one digit, and one symbol
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the password list to remove predictability
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("==== Password Generator ====")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
