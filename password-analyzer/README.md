# Password Strength Analyzer

A Python-based cybersecurity tool designed to evaluate password strength, detect weak patterns, check against leaked datasets, and estimate password crack time.

---

## Overview

This project analyzes user-provided passwords by evaluating their strength using multiple security criteria. It also checks whether the password exists in a commonly used leaked dataset and estimates how long it would take to crack the password using brute-force assumptions.

Additionally, the tool provides actionable suggestions to improve weak passwords and can generate secure passwords.

---

## Features

* Password strength classification (Weak, Medium, Strong)
* Actionable suggestions to improve password security
* Secure password hashing using SHA-256
* Detection of common passwords using a leaked dataset (rockyou.txt)
* Case-insensitive comparison for improved detection accuracy
* Estimated password crack time calculation
* Detection of weak patterns:

  * Sequential numbers (e.g., 123, 456)
  * Sequential letters (e.g., abc, xyz)
  * Repeated characters
  * Common words like "password"
* Secure password generator
* Command-line interface (CLI) menu system
* Modular code structure with separation of concerns
* Error handling for missing dataset files

---

## How It Works

1. The user selects an option from the menu:

   * Analyze a password
   * Generate a password
2. For password analysis:

   * The password is hashed using SHA-256
   * The system checks if the password exists in a leaked dataset
   * Strength is evaluated based on:

     * Length
     * Uppercase and lowercase characters
     * Numeric digits
     * Special characters
   * Weak patterns are detected
   * Suggestions are provided for improvement
   * Estimated crack time is calculated
3. For password generation:

   * A strong password is generated using a mix of character types

---

## Project Structure

password-analyzer/
│
├── password_analyzer.py   # Main application (CLI interface)
├── utils.py               # Core logic and utility functions
├── rockyou.txt            # Optional leaked password dataset
├── .gitignore
└── README.md

---

## Installation and Setup

### 1. Clone the repository

git clone https://github.com/MANOJ-R-223/password-analyzer.git
cd password-analyzer

### 2. Download the dataset (optional)

Download the rockyou.txt dataset and place it in the project directory.

Note: The dataset is not included in this repository due to its large size.

---

## Usage

Run the program:

python password_analyzer.py

---

## Menu Options

====== PASSWORD ANALYZER ======

1. Enter Password
2. Generate Password
3. Exit

---

## Example Output

Loading common passwords...

Enter password: Password123!

SHA-256 Hash: <hashed_value>

Weak Patterns Detected:

* Contains sequential numbers

Strength: Medium

Suggestions to improve:

* Add special characters

Estimated crack time: 2 days

---

## Technologies Used

* Python
* Regular Expressions (re module)
* Hashing (SHA-256 via hashlib)
* Random and String modules
* File Handling

---

## Future Enhancements

* Graphical user interface (GUI)
* Web-based interface (Flask or Django)
* Advanced entropy-based scoring
* Keyboard pattern detection (e.g., qwerty, asdf)
* Password strength visualization

---

## Author

MANOJ R

---

## Disclaimer

This project is intended for educational purposes only. It should not be used for any unauthorized or malicious activities.
