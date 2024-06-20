import random
import string

def generate_password(length):
    # Define the character sets to use
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Get the desired length of the password from the user
    length = get_user_input()
    # Generate the password
    password = generate_password(length)
    # Display the password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
