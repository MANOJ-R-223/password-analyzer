# Password Strength Analyzer

A Python-based cybersecurity tool designed to evaluate password strength and detect weak passwords using real-world leaked datasets.

---

## Overview

This project analyzes user-provided passwords by evaluating their strength based on multiple criteria and checking whether they exist in a commonly used leaked password dataset. It also generates a secure hash of the password using SHA-256.

---

## Features

- Password strength classification (Weak, Medium, Strong)
- Secure password hashing using SHA-256
- Detection of common passwords using a leaked dataset (rockyou.txt)
- Case-insensitive comparison for improved detection accuracy
- Modular code structure with separation of concerns
- Error handling for missing dataset files

---

## How It Works

1. The user inputs a password
2. The password is hashed using the SHA-256 algorithm
3. The program evaluates password strength based on:
   - Minimum length
   - Presence of uppercase and lowercase characters
   - Inclusion of numeric digits
   - Use of special characters
4. The password is compared against a leaked dataset to determine if it is commonly used

---

## Project Structure

password-analyzer/
│
├── password_analyzer.py   # Main application entry point
├── utils.py               # Utility functions and core logic
├── .gitignore
└── README.md

---

## Installation and Setup

### 1. Clone the repository

git clone https://github.com/MANOJ-R-223/password-analyzer.git  
cd password-analyzer  

### 2. Download the dataset

Download the rockyou.txt dataset and place it in the project directory.

Note: The dataset is not included in this repository due to its large size.

---

## Usage

python password_analyzer.py

---

## Example Output

Loading common passwords...

Enter password: Password123!

SHA-256 Hash: <hashed_value>

Strength: Strong

---

## Notes

- If the dataset file (rockyou.txt) is not present, the program will still function
- In such cases, the leaked password detection feature will be skipped

---

## Technologies Used

- Python
- Regular Expressions (re module)
- Hashing (SHA-256 via hashlib)
- File Handling

---

## Future Enhancements

- Password improvement suggestions
- Estimated password crack time calculation
- Command-line interface (CLI) menu system
- Web-based interface

---

## Author

MANOJ R

---

## Disclaimer

This project is intended for educational purposes only. It should not be used for any unauthorized or malicious activities.