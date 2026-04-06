def check_password(password):
    if len(password)<6:
        return "Weak"
    else:
        return "Strong"
    
print(check_password("password"))