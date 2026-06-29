import os
import subprocess
import sqlite3
import hashlib

# VULNERABILITY 1: Command Injection
def ping_host():
    host = input("Enter IP to ping: ")
    # DANGER: User input directly in system command
    os.system("ping " + host)  # <-- Semgrep WILL catch this!

# VULNERABILITY 2: Hardcoded Password (Secret Leak)
ADMIN_PASSWORD = "admin123"  # <-- Semgrep WILL catch this!
SECRET_KEY = "my_super_secret_key_12345"  # <-- Semgrep WILL catch this!

# VULNERABILITY 3: SQL Injection
def get_user():
    user_id = input("Enter user ID: ")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # DANGER: String concatenation in SQL query
    query = "SELECT * FROM users WHERE id = " + user_id  # <-- Semgrep WILL catch this!
    cursor.execute(query)
    return cursor.fetchone()

# VULNERABILITY 4: Weak Hash Algorithm
def hash_password(password):
    # DANGER: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()  # <-- Semgrep WILL catch this!

# VULNERABILITY 5: Use of eval() - Dangerous
def process_data():
    data = input("Enter data: ")
    # DANGER: eval() can execute arbitrary code
    result = eval(data)  # <-- Semgrep WILL catch this!
    return result

# VULNERABILITY 6: Pickle with untrusted data
import pickle

def load_config():
    filename = input("Enter config file: ")
    # DANGER: Loading pickle from untrusted source
    with open(filename, 'rb') as f:
        config = pickle.load(f)  # <-- Semgrep WILL catch this!
    return config

# VULNERABILITY 7: Insecure file permissions
def create_temp_file():
    import tempfile
    # DANGER: Insecure file permissions
    tempfile.mktemp()  # <-- Semgrep WILL catch this!

if __name__ == "__main__":
    ping_host()
    get_user()
    hash_password("test")
    process_data()
    load_config()
    create_temp_file()
    print("All done!")
