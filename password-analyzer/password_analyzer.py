from utils import check_password, hash_password, load_common_passwords, is_common_password

common_passwords = load_common_passwords()
pwd = input("Enter password: ")
print("Strength:", check_password(pwd))
print("Hash:", hash_password(pwd))

if is_common_password(pwd, common_passwords):
    print("Your password is found in leaked dataset")