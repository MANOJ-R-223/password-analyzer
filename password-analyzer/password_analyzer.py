import time
from utils import check_password, hash_password, load_common_passwords, is_common_password, estimate_crack_time, generate_password, detect_patterns

def main():
    print("\nLoading common passwords...")
    common_passwords = load_common_passwords()

    if not common_passwords:
        print("Dataset not loaded. Skipping leak check.")

    while True:
        print("\n" + "="*40)
        print("           PASSWORD ANALYZER")
        print("="*40)
        print("1. Enter Password")
        print("2. Generate Password")
        print("3. Exit")

        choice = input("\nEnter choice : ")

        if choice == "1":

            pwd = input("\nEnter password: ")
            print("\nAnalyzing password", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print()

            print(f"\nHash                : {hash_password(pwd)}")

            patterns = detect_patterns(pwd)

            if patterns:
                print("\n[!] Weak Patterns Detected:")
                for p in patterns:
                    print("-", p)

            if common_passwords and is_common_password(pwd, common_passwords):
                print("\nWeak Password       : Found in leaked dataset")
            else:
                strength, suggestions = check_password(pwd)
                print(f"\nStrength            : {strength}")

                if suggestions:
                    print("\nSuggestions to improve:")
                    for s in suggestions:
                        print(f" - {s}")
    
            print(f"\nEstimated Crack Time: {estimate_crack_time(pwd)}")

        elif choice == "2":
            try: 
                length = int(input("Enter desired password length : "))
                print(f"\nGenerated Password : {generate_password(length)}")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "3":
            print("\nExiting....")
            break

        else:
            print("Invalid Option. Try Again")

        print("\n" + "-"*40)
            


if __name__ == "__main__":
    main()