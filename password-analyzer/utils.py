import hashlib
import re
import random
import string

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include Numbers")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Use special characters (!@#$...)")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    return strength, suggestions


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

def estimate_crack_time(password):
    charset_size = 0

    if re.search(r"[a-z]",password):
        charset_size += 26
    if re.search(r"[A-Z]",password):
        charset_size += 26
    if re.search(r"[0-9]",password):
        charset_size += 10
    if re.search(r"[^a-zA-Z0-9]",password):
        charset_size += 32

    length = len(password)

    combinations = charset_size ** length

    guesses_per_sec = 1000000

    seconds = combinations/guesses_per_sec

    return format_time(seconds)

def format_time(seconds):
    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    else:
        return f"{int(seconds // 31536000)} years"
    
def generate_password(length = 12):
    if length < 6:
        return "Password length should be at least 6"

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"

    password = [random.choice(lower),random.choice(upper),random.choice(digits),random.choice(special)]
    all_char = lower + upper + digits + special
    password += random.choices(all_char,k=length-4)
    random.shuffle(password)

    return "".join(password)

