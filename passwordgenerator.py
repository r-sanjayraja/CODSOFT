import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
