from utils import check_password, hash_password, load_common_passwords, is_common_password, estimate_crack_time

def main():
    print("\nLoading common passwords...")
    common_passwords = load_common_passwords()

    if not common_passwords:
        print("Dataset not loaded. Skipping leak check.")

    pwd = input("\nEnter password: ")
    print("\nSHA-256 Hash:", hash_password(pwd))

    if common_passwords and is_common_password(pwd, common_passwords):
        print("\nWeak Password : Your password is found in leaked dataset")
    else:
        strength, suggestions = check_password(pwd)
        print("\nStrength :",strength)

        if suggestions:
            print("\nSuggestions to improve:")
            for s in suggestions:
                print("\n->",s)
    
    print("\nEstimated crack time: ", estimate_crack_time(pwd))


if __name__ == "__main__":
    main()