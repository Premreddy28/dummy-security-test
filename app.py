import os

def get_user_input():
    return input("Enter your name: ")

def vulnerable_function():
    user_name = get_user_input()
    # Command injection vulnerability!
    os.system("echo Hello " + user_name)

def safe_function():
    print("Hello, World!")

if __name__ == "__main__":
    vulnerable_function()
