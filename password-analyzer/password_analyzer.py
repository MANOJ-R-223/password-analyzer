from utils import check_password

pwd = input("Enter password: ")
print("Strength:", check_password(pwd))