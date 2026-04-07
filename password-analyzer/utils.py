import hashlib
import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_common_passwords():
    passwords = set()
    try:
        with open("rockyou.txt", "r", encoding="latin-1") as file:
            for line in file:
                passwords.add(line.strip())
    except FileNotFoundError:
        return set()

    return passwords

def is_common_password(password, common_passwords):
    return password.lower() in common_passwords